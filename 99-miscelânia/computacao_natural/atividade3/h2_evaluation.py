import helpers
import kapa
import sys
import csv

def print_shape(shape):
    x = -1
    for i in range(12):
        row = ''
        for j in range(10):
            x += 1
            if shape[x]:
                row += 'X'
            else:
                row += ' '
        print row

results = []

for i in range(1, 11):
    for _ in range(30):
        result = kapa.kapa(
            antigens             = [kapa.Antibody() for _ in range(i)],
            antibodies           = [kapa.Antibody() for _ in range(10)],
            generations          = 100,
            num_clone_antibodies = 5,
            num_kill_antibodies  = 0,
            clone_multiplier     = 10
        )
        print result
        results.append({
            'antigens' : i,
            'generations' : result
        })
with open('output.csv', 'wb') as output_csv:
    dict_writer = csv.DictWriter(output_csv, ['antigens', 'generations'])
    dict_writer.writeheader()
    dict_writer.writerows(results)
sys.exit()

with open('output.csv', 'wb') as output_csv:
    dict_writer = csv.DictWriter(output_csv, ['generation', 'key', 'affinity'])
    dict_writer.writeheader()
    dict_writer.writerows(affinity_graph)

sys.exit()
for antibody in best_antibodies:
    print_shape(antibody.shape)
