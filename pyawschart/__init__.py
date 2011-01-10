import math
import boto
from datetime import datetime, timedelta

from pygooglechart import Chart
from pygooglechart import SimpleLineChart
from pygooglechart import Axis


RANGES = {
    'hour': { 'timedelta': timedelta(hours=1), 'period': 60, 'period_verbose': '1 min avg' }, # 1 minute average
    'day': { 'timedelta': timedelta(days=1), 'period': 60*5, 'period_verbose': '5 min avg' }, # 5 minute average
    'week': { 'timedelta': timedelta(days=7), 'period': 60*30, 'period_verbose': '30 min avg' }, # 30 minute average
    'month': { 'timedelta': timedelta(days=30), 'period': 60*60, 'period_verbose': '1 hr avg' }, # 1 hour average
}


def convert_bytes(bytes):
    bytes = float(bytes)
    if bytes >= 1099511627776:
        terabytes = bytes / 1099511627776
        size = '%.2fT' % terabytes
    elif bytes >= 1073741824:
        gigabytes = bytes / 1073741824
        size = '%.2fG' % gigabytes
    elif bytes >= 1048576:
        megabytes = bytes / 1048576
        size = '%.2fM' % megabytes
    elif bytes >= 1024:
        kilobytes = bytes / 1024
        size = '%.2fK' % kilobytes
    else:
        size = '%.2fb' % bytes
    return size


def round_float(f):
    f = float(f)
    if f > 1.0:
        rounded = '%.1f' % f
    elif f > 0.1:
        rounded = '%.2f' % f
    elif f > 0.01:
        rounded = '%.3f' % f
    else:
        rounded = '%.4f' % f
    return rounded


class AWSChart(object):

    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        self.cloudwatch_connection = cloudwatch_connection
        self.instance = instance
        self.range = range
        self.metric_verbose = None
        self.period_verbose = range['period_verbose']
        self.args = dict()
        self.args['period'] = range['period']
        self.args['end_time'] = datetime.now()
        self.args['start_time'] = self.args['end_time'] - range['timedelta']
        self.args['metric'] = None
        self.args['namespace'] = None
        self.args['statistics'] = None
        self.args['dimensions'] = None
        self.args['unit'] = None
        self.max = None
        self.min = None
        self._datapoints = None
        self._chart = None

    def _get_datapoints(self):
        if not self._datapoints:
            self._datapoints = self.cloudwatch_connection.get_metric_statistics(
                self.args['period'],
                self.args['start_time'],
                self.args['end_time'], 
                self.args['metric'],
                self.args['namespace'],
                self.args['statistics'],
                self.args['dimensions'],
                self.args['unit']
            )
        return self._datapoints
    
    def _get_chart(self):
        if not self._chart:
            datapoints = self._get_datapoints()
            data = [datapoint['Average'] for datapoint in self._datapoints]
        
            # Set the vertical range from 0 to 100
            max_y = 1
            if data:
                max_y = max(data)*1.1
            
            # max_y cannot be zero
            if max_y == 0:
                max_y = 1
            
            # Make sure percentage doesn't exceed 100%
            if self.args['unit'] == 'Percent':
                max_y = 100
    
            # Chart size of 300x125 pixels and specifying the range for the Y axis
            chart = SimpleLineChart(380, 125, y_range=[0, max_y])
        
            # Add the chart data
            chart.add_data(data)
            chart.add_data([0, 0])
        
            # Set the line colour to blue
            chart.set_colours(['0000FF', '76A4FB'])
            
            # Fill below data line
            chart.add_fill_range('76A4FB', 0, 1)
        
            # Set the horizontal dotted lines
            chart.set_grid(0, 25, 5, 5)
        
            # The Y axis labels contains 0 to 100 skipping every 25, but remove the
            # first number because it's obvious and gets in the way of the first X
            # label.
            step = (max_y*1.0)/4
            if not step:
                step = 1
            #left_axis = range(0, max_y + 1, step)
            left_axis = []
            left_axis.append('')
            left_axis.append(step)
            left_axis.append(step*2)
            left_axis.append(step*3)
            left_axis.append(step*4)
            
            i = 1
            if self.args['unit'] == 'Percent':
                for point in left_axis[1:]:
                    left_axis[i] = '%s%%' % left_axis[i]
                    i = i + 1
            elif self.args['unit'] == 'Bytes':
                for point in left_axis[1:]:
                    left_axis[i] = convert_bytes(int(left_axis[i]))
                    i = i + 1
            elif self.args['unit'] == 'Bytes/Second':
                for point in left_axis[1:]:
                    left_axis[i] = '%s/s' % convert_bytes(int(left_axis[i]))
                    i = i + 1
            elif self.args['unit'] == 'Seconds':
                for point in left_axis[1:]:
                    left_axis[i] = '%ss' % round_float(left_axis[i])
                    i = i + 1
            elif self.args['unit'] == 'Count/Second':
                for point in left_axis[1:]:
                    left_axis[i] = '%s/s' % round_float(left_axis[i])
                    i = i + 1
    
            chart.set_axis_labels(Axis.LEFT, left_axis)
            
            # X axis labels
            bottom_axis = []
            
            # hourly chart
            if self.range['timedelta'] == timedelta(hours=1):
                bottom_axis.append(self.args['start_time'].strftime('%H:%M'))
                bottom_axis.append((self.args['end_time'] - timedelta(minutes=45)).strftime('%H:%M'))
                bottom_axis.append((self.args['end_time'] - timedelta(minutes=30)).strftime('%H:%M'))
                bottom_axis.append((self.args['end_time'] - timedelta(minutes=15)).strftime('%H:%M'))
                bottom_axis.append(self.args['end_time'].strftime('%H:%M'))
            
            # daily chart
            if self.range['timedelta'] == timedelta(days=1):
                bottom_axis.append(self.args['start_time'].strftime('%H:%M'))
                bottom_axis.append((self.args['end_time'] - timedelta(hours=18)).strftime('%H:%M'))
                bottom_axis.append((self.args['end_time'] - timedelta(hours=12)).strftime('%H:%M'))
                bottom_axis.append((self.args['end_time'] - timedelta(hours=6)).strftime('%H:%M'))
                bottom_axis.append(self.args['end_time'].strftime('%H:%M'))
            
            # weekly chart
            if self.range['timedelta'] == timedelta(days=7):
                bottom_axis.append(self.args['start_time'].strftime('%d'))
                bottom_axis.append((self.args['end_time'] - timedelta(days=6)).strftime('%d'))
                bottom_axis.append((self.args['end_time'] - timedelta(days=5)).strftime('%d'))
                bottom_axis.append((self.args['end_time'] - timedelta(days=4)).strftime('%d'))
                bottom_axis.append((self.args['end_time'] - timedelta(days=3)).strftime('%d'))
                bottom_axis.append((self.args['end_time'] - timedelta(days=2)).strftime('%d'))
                bottom_axis.append((self.args['end_time'] - timedelta(days=1)).strftime('%d'))
                bottom_axis.append(self.args['end_time'].strftime('%d'))
                
            # monthly chart
            if self.range['timedelta'] == timedelta(days=30):
                bottom_axis.append(self.args['start_time'].strftime('%d'))
                bottom_axis.append((self.args['end_time'] - timedelta(days=25)).strftime('%d'))
                bottom_axis.append((self.args['end_time'] - timedelta(days=20)).strftime('%d'))
                bottom_axis.append((self.args['end_time'] - timedelta(days=15)).strftime('%d'))
                bottom_axis.append((self.args['end_time'] - timedelta(days=10)).strftime('%d'))
                bottom_axis.append((self.args['end_time'] - timedelta(days=5)).strftime('%d'))
                bottom_axis.append(self.args['end_time'].strftime('%d'))
     
            chart.set_axis_labels(Axis.BOTTOM, bottom_axis)
        
            self._chart = chart
        return self._chart
        
            
    def get_url(self):
        chart = self._get_chart()
        return chart.get_url()


    def download(self, filename):
        chart = self._get_chart()
        return chart.download(filename)