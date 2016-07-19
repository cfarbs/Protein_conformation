#!/usr/bin/env python

import helix_runner_v1
import testdefault_random_Models.stat_reader

args = helix_runner_v1.parse_args()

for i in range(10):
    helix_runner_v1.main(args)
    testdefault_random_Models.stat_reader
