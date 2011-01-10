from pyawschart import AWSChart


CHART_CLASSES = []


class EC2Chart(AWSChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        AWSChart.__init__(self, cloudwatch_connection, instance, range)
        self.args['namespace'] = 'AWS/EC2'
        self.args['dimensions'] = { 'VolumeId': instance }

        
class CPUUtilizationChart(EC2Chart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        EC2Chart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'CPU utilization'
        self.args['metric'] = 'CPUUtilization'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Percent'
CHART_CLASSES.append(CPUUtilizationChart)


class NetworkInChart(EC2Chart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        EC2Chart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Network in'
        self.args['metric'] = 'NetworkIn'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Bytes/Second'
CHART_CLASSES.append(NetworkInChart)


class NetworkOutChart(EC2Chart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        EC2Chart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Network out'
        self.args['metric'] = 'NetworkOut'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Bytes/Second'
CHART_CLASSES.append(NetworkOutChart)


class DiskReadOpsChart(EC2Chart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        EC2Chart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Disk read operations'
        self.args['metric'] = 'DiskReadOps'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Count/Second'
CHART_CLASSES.append(DiskReadOpsChart)


class DiskReadBytesChart(EC2Chart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        EC2Chart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Disk read bytes'
        self.args['metric'] = 'DiskReadBytes'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Bytes/Second'
CHART_CLASSES.append(DiskReadBytesChart)


class DiskWriteOpsChart(EC2Chart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        EC2Chart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Disk write operations'
        self.args['metric'] = 'DiskWriteOps'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Count/Second'
CHART_CLASSES.append(DiskWriteOpsChart)


class DiskWriteBytesChart(EC2Chart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        EC2Chart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Disk write bytes'
        self.args['metric'] = 'DiskWriteBytes'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Bytes/Second'
CHART_CLASSES.append(DiskWriteBytesChart)