from pyawschart import AWSChart


CHART_CLASSES = []


class ELBChart(AWSChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        AWSChart.__init__(self, cloudwatch_connection, instance, range)
        self.args['namespace'] = 'AWS/ELB'
        self.args['dimensions'] = { 'LoadBalancerName': instance }

        
class LatencyChart(ELBChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        ELBChart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Latency'
        self.args['metric'] = 'Latency'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Seconds'
CHART_CLASSES.append(LatencyChart)

    
class RequestCountChart(ELBChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        ELBChart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Request count'
        self.args['metric'] = 'RequestCount'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Count/Second'
CHART_CLASSES.append(RequestCountChart)


class HealthyHostCountChart(ELBChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        ELBChart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Healthy host count'
        self.args['metric'] = 'HealthyHostCount'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Count'
CHART_CLASSES.append(HealthyHostCountChart)


class UnHealthyHostCountChart(ELBChart):
    def __init__(self, cloudwatch_connection=None, instance=None, range=None):
        ELBChart.__init__(self, cloudwatch_connection, instance, range)
        self.metric_verbose = 'Unhealthy host count'
        self.args['metric'] = 'UnHealthyHostCount'
        self.args['statistics'] = 'Average'
        self.args['unit'] = 'Count'
CHART_CLASSES.append(UnHealthyHostCountChart)