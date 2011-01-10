from pyawschart import AWSChart


CHART_CLASSES = []


class RDSChart(AWSChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        AWSChart.__init__(self, cloudwatch_connection, instance, range)
        self.args['namespace'] = 'AWS/RDS'
        self.args['dimensions'] = { 'DBInstanceIdentifier': instance }

        
class CPUUtilizationChart(RDSChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        RDSChart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'CPU utilization'
        self.args['metric'] = 'CPUUtilization'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Percent'
CHART_CLASSES.append(CPUUtilizationChart)


class DatabaseConnectionsChart(RDSChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        RDSChart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Database connections'
        self.args['metric'] = 'DatabaseConnections'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Count/Second'
CHART_CLASSES.append(DatabaseConnectionsChart)


class FreeableMemoryChart(RDSChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        RDSChart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Freeable memory'
        self.args['metric'] = 'FreeableMemory'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Bytes'
CHART_CLASSES.append(FreeableMemoryChart)


class SwapUsageChart(RDSChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        RDSChart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Swap usage'
        self.args['metric'] = 'SwapUsage'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Bytes'      
CHART_CLASSES.append(SwapUsageChart)


class FreeStorageSpaceChart(RDSChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        RDSChart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Free storage space'
        self.args['metric'] = 'FreeStorageSpace'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Bytes'
CHART_CLASSES.append(FreeStorageSpaceChart)


class BinLogDiskUsageChart(RDSChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        RDSChart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Binlog disk usage'
        self.args['metric'] = 'BinLogDiskUsage'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Bytes'
CHART_CLASSES.append(BinLogDiskUsageChart)


class ReadIOPSChart(RDSChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        RDSChart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Read I/O operations'
        self.args['metric'] = 'ReadIOPS'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Count/Second'
CHART_CLASSES.append(ReadIOPSChart)


class ReadThroughputChart(RDSChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        RDSChart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Read throughput'
        self.args['metric'] = 'ReadThroughput'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Bytes/Second'
CHART_CLASSES.append(ReadThroughputChart)


class ReadLatencyChart(RDSChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        RDSChart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Read latency'
        self.args['metric'] = 'ReadLatency'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Seconds'
CHART_CLASSES.append(ReadLatencyChart)


class WriteIOPSChart(RDSChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        RDSChart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Write I/O operations'
        self.args['metric'] = 'WriteIOPS'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Count/Second'
CHART_CLASSES.append(WriteIOPSChart)


class WriteThroughputChart(RDSChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        RDSChart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Write throughput'
        self.args['metric'] = 'WriteThroughput'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Bytes/Second'
CHART_CLASSES.append(WriteThroughputChart)


class WriteLatencyChart(RDSChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        RDSChart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Write latency'
        self.args['metric'] = 'WriteLatency'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Seconds'
CHART_CLASSES.append(WriteLatencyChart)
