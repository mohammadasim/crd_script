"""
    When upgrading the prometheus operator we
    need to create CRDS each time. This script
    will automate the applying of those CRDS.
    If you are making a change to Prometheus
    Operator, and you get probeNamespaceSelector
    error, run this script and then execute
    the command that failed again and the
    error will be gone.
"""
# !/usr/bin/env python3

import os

crd_list = [
    'https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.42.0/example/prometheus-operator'
    '-crd/monitoring.coreos.com_alertmanagers.yaml',
    'https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.42.0/example/prometheus-operator'
    '-crd/monitoring.coreos.com_podmonitors.yaml',
    'https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.42.0/example/prometheus-operator'
    '-crd/monitoring.coreos.com_probes.yaml',
    'https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.42.0/example/prometheus-operator'
    '-crd/monitoring.coreos.com_prometheuses.yaml',
    'https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.42.0/example/prometheus-operator'
    '-crd/monitoring.coreos.com_prometheusrules.yaml',
    'https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.42.0/example/prometheus-operator'
    '-crd/monitoring.coreos.com_servicemonitors.yaml',
    'https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.42.0/example/prometheus-operator'
    '-crd/monitoring.coreos.com_thanosrulers.yaml',
]


def apply_crds(crds: list) -> None:
    """
    Function to iterate over the list
    and apply the crds
    """
    for crd in crds:
        os.system(f'kubectl apply -f {crd}')


if __name__ == '__main__':
    apply_crds(crd_list)
