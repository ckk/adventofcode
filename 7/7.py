#!/usr/bin/env python

import re

def assemble(input_file):
    with open(input_file) as f:
        instructions = [s.strip() for s in f.readlines()]
    connections = dict()
    for instr in instructions:
        what, assignee = re.match(r"^(.+) -> (\D+)$", instr).groups()
        # just a connection / assignment
        if re.match(r"^[a-z\d]+$", what) is not None:
            connections[assignee] = {'op': 'ASSIGN', 'right': what}
            continue;
        # operations
        op_match = re.match(r"^(\w+)?.*(NOT|LSHIFT|RSHIFT|AND|OR) (\w+)", what)
        if op_match is not None:
            (left, op, right) = op_match.groups()
            connections[assignee] = {'op': op, 'left': left, 'right': right}
            continue
        print("ERROR: Unhandled: assignee: %s, what: %s" % (assignee, what))
    return connections

def value(wires, conn, which):
    if which in conn:
        try:
            return int(conn[which])
        except:
            if conn[which] in wires:
                return wires[conn[which]]
    return None

def emulate(connections):
    # thought about building a graph first, but tried this simple approach first and for
    # the given input it's pretty fast. Was even faster in my first version that only
    # dealt with input as given, this version should handle any instruction/operand input.
    wires = dict()
    while len(connections) > 0:
         last = len(connections)
         for assignee, conn in connections.items():
             keep = False
             left = value(wires, conn, 'left')
             right = value(wires, conn, 'right')
             # could use function pointers or similar to handle the operators
             # with two operands in a generic way
             if conn['op'] == 'ASSIGN' and right is not None:
                 wires[assignee] = right
             elif conn['op'] == 'NOT' and right is not None:
                 wires[assignee] = ~right & 65535
             elif conn['op'] == 'LSHIFT' and left is not None: # right is always an int
                 wires[assignee] = left << right & 65535
             elif conn['op'] == 'RSHIFT' and left is not None: # "
                 wires[assignee] = left >> right
             elif left is not None and right is not None:
                 if conn['op'] == 'AND':
                     wires[assignee] = left & right
                 elif conn['op'] == 'OR':
                     wires[assignee] = left | right
             else:
                 keep = True
             if not keep:
                 wires[assignee] = wires[assignee]
                 del connections[assignee]
    return wires
      
# test
input_test_connections = assemble('input-test')
print(emulate(input_test_connections))

# part 1
input_connections = assemble('input')
output_wires = emulate(input_connections.copy())
print("a: %d" % output_wires['a'])

# part 2
input_connections['b'] = {'left': None, 'op': 'ASSIGN', 'right': output_wires['a']}
output_wires_2 = emulate(input_connections)
print("new a: %d" % output_wires_2['a'])
