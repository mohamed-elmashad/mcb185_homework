import gzip
import json
import sys

def read_transfac(filename):
	with gzip.open(filename, 'rt') as fp:
		records = []
		pwm = None
		
		for line in fp:
			line = line.strip()
			if not line or line.startswith("//"):
				if pwm:
					records.append(pwm)
				continue

			if line.startswith('ID'):
				pwm_id = line.split()[1]
				pwm = {"id": pwm_id, "pwm": []}
			elif pwm and line.startswith('XX'):
				continue
			elif pwm and not line.startswith('PO'):
				parts = line.split()
				if len(parts) == 5 and parts[0].isdigit():
					pwm["pwm"].append({})
					pwm["pwm"][-1]["A"] = parts[1]
					pwm["pwm"][-1]["C"] = parts[2]
					pwm["pwm"][-1]["G"] = parts[3]
					pwm["pwm"][-1]["T"] = parts[4]
		fp.close()
		return records
	
filename = sys.argv[1]
pwm_records = read_transfac(filename)
print(json.dumps(pwm_records, indent=4))
