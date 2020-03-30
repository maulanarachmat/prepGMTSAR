import os, sys

master = sys.argv[1]
slave = sys.argv[2]


for (dirname, dirs, files) in os.walk(master):
   #os.system(createdir)
	for filename in files:
		if filename.endswith('.xml') and filename.startswith('T'):
			master_meta = os.path.join(dirname,filename)
			
			master_target = filename.split('_')[0][:3]+filename.split('_')[-1][:8]
			print(master_target)
			print(master_meta)
		if filename.endswith('.cos'):
			master_img = os.path.join(dirname,filename)
			print(master_img)

for (dirname, dirs, files) in os.walk(slave):
   #os.system(createdir)
	for filename in files:
		if filename.endswith('.xml') and filename.startswith('T'):
			slave_meta = os.path.join(dirname,filename)
			slave_target = filename.split('_')[0][:3]+filename.split('_')[-1][:8]
			print(slave_target)
			print(slave_meta)
		if filename.endswith('.cos'):
			slave_img = os.path.join(dirname,filename)
			print(slave_img)

with open('README.txt', 'w') as f:
	f.write('cd raw \n')
	f.write('ln -s %s ./%s.xml \n' %(master_meta, master_target))
	f.write('ln -s %s ./%s.cos \n \n' %(master_img, master_target))
	
	f.write('ln -s %s ./%s.xml \n' %(slave_meta, slave_target))
	f.write('ln -s %s ./%s.cos \n \n' %(slave_img, slave_target))
	
	f.write('make_slc_tsx %s.xml %s.cos %s \n' %(master_target, master_target, master_target))
	f.write('make_slc_tsx %s.xml %s.cos %s \n\n' %(slave_target, slave_target, slave_target))
	
	f.write('cd .. \n')
	f.write('p2p_TSX_SLC.csh %s %s config.tsx.txt' %(master_target, slave_target))