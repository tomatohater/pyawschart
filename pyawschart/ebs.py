from pyawschart import AWSChart


CHART_CLASSES = []


class EBSChart(AWSChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        AWSChart.__init__(self, cloudwatch_connection, instance, range)
        self.args['namespace'] = 'AWS/EBS'
        self.args['dimensions'] = { 'VolumeId': instance }

        
class VolumeReadBytesChart(EBSChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        EBSChart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Volume read bytes'
        self.args['metric'] = 'VolumeReadBytes'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Bytes/Second'
CHART_CLASSES.append(VolumeReadBytesChart)  


class VolumeReadOpsChart(EBSChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        EBSChart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Volume read operations'
        self.args['metric'] = 'VolumeReadOps'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Count/Second'
CHART_CLASSES.append(VolumeReadOpsChart)


class VolumeTotalReadTimeChart(EBSChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        EBSChart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Volume total read time'
        self.args['metric'] = 'VolumeTotalReadTime'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Seconds'
CHART_CLASSES.append(VolumeTotalReadTimeChart)


class VolumeWriteBytesChart(EBSChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        EBSChart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Volume write bytes'
        self.args['metric'] = 'VolumeWriteBytes'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Bytes/Second'
CHART_CLASSES.append(VolumeWriteBytesChart)

    
class VolumeWriteOpsChart(EBSChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        EBSChart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Volume write operations'
        self.args['metric'] = 'VolumeWriteOps'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Count/Second'
CHART_CLASSES.append(VolumeWriteOpsChart)


class VolumeTotalWriteTimeChart(EBSChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        EBSChart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Volume total write time'
        self.args['metric'] = 'VolumeTotalWriteTime'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Seconds'
CHART_CLASSES.append(VolumeTotalWriteTimeChart)


class VolumeIdleTimeChart(EBSChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        EBSChart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Volume idle time'
        self.args['metric'] = 'VolumeIdleTime'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Seconds'
CHART_CLASSES.append(VolumeIdleTimeChart)


class VolumeQueueLengthChart(EBSChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        EBSChart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Volume queue length'
        self.args['metric'] = 'VolumeQueueLength'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Count'
CHART_CLASSES.append(VolumeQueueLengthChart)