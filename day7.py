
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = {} #{name:File}
        self.subdirs = {} #{name:Dir} 
    
    def get_size(self):
        size = sum([f.size for f in self.files.values()])
        size += sum([d.get_size() for d in self.subdirs.values()])
        return size

with open('day7_input.txt','r') as f:
    lines = f.readlines()
lines = [l.rstrip() for l in lines]

topDir = Dir('/', None)
currentDir = None
for line in lines:
    if line[0] == '$': 
        cmd = line.split(' ')[1]
        if cmd == 'cd':
            arg = line.split(' ')[2]
            if arg == '..':
                currentDir = currentDir.parent
            elif arg == '/':
                currentDir = topDir
            else:
                if arg in currentDir.subdirs.keys():
                    currentDir = currentDir.subdirs[arg]
                else:
                    raise Exception('dir has not yet been discovered')
        elif cmd == 'ls':
            pass
    elif len(line)>3 and line[:3] == 'dir':
        name = line.replace('dir ','')
        if name not in currentDir.subdirs.keys():
            currentDir.subdirs.update({name: Dir(name, currentDir)})
    elif line[0].isdigit():
        size, name = line.split(' ')
        currentDir.files.update({name: File(name, int(size))})

def collect_dirs(topDir, dirs_list=[]):
    dirs_list.append(topDir) 
    for subDir in topDir.subdirs.values():
        collect_dirs(subDir, dirs_list)
    return dirs_list

dirs = collect_dirs(topDir)
print(sum([d.get_size() for d in dirs if d.get_size()<100000]))

#bonus
requiredFreeMem = 30000000
totalMem = 70000000
freeMem = 70000000 - topDir.get_size()
toDelete = requiredFreeMem - freeMem 
print(f'delete target: {toDelete}')
dirs = [d for d in dirs if d.get_size() >= toDelete]
dirs.sort(key=lambda x:x.get_size())
deleteDir = dirs[0]
print(deleteDir.name, deleteDir.get_size())
