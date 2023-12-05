import subprocess

cmd_version = 'git show -s'

def process_command(cmd):
    return cmd.split(' ')


def get_software_version():
    cmd = process_command(cmd_version)
    with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as proc:
        lines = proc.stdout.readlines()
        for index, line in enumerate(lines):
            lines[index] = line.decode('ascii').rstrip("\n")
    
        lines.insert(0, "\nSoftware version:\n")
        lines.append("\n")
        
    return lines

if __name__ == "__main__":
    print(get_software_version())