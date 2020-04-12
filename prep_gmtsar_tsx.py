import os, sys

def gt_fl(inp):
	for root, dirs, files in os.walk(inp):
		for filename in files:
			if filename.endswith('.xml') and filename.startswith('T'):
				inp_meta = os.path.join(os.path.abspath(root), filename)
				inp_target = filename.split('_')[0][:3]+filename.split('_')[-1][:8]
			if filename.endswith('.cos'):
				inp_img = os.path.join(os.path.abspath(root),filename)
	return inp_meta, inp_img, inp_target

if __name__ == '__main__':
	master = sys.argv[1]
	slave = sys.argv[2]
	master_meta, master_img, master_target = gt_fl(master)
	slave_meta, slave_img, slave_target = gt_fl(slave)
	print("Created README File For : %s %s" %(master_target,slave_target))

	with open('README.txt', 'w') as f:
		f.write('cd raw \n')
		f.write('ln -s %s ./%s.xml \n' %(master_meta, master_target))
		f.write('ln -s %s ./%s.cos \n \n' %(master_img, master_target))
		
		f.write('ln -s %s ./%s.xml \n' %(slave_meta, slave_target))
		f.write('ln -s %s ./%s.cos \n \n' %(slave_img, slave_target))
		
		f.write('## Check Your GMTSAR Version and Which Code Supports on Your System. \n')
		f.write('## Do Comment/Uncomment("#") Your Selection \n \n')
		
		f.write('##(1)\n')
		f.write('#cd .. \n')
		f.write('#p2p_processing.csh TSX %s %s \n \n' %(master_target, slave_target))
		
		f.write('##(2)\n')
		f.write('make_slc_tsx %s.xml %s.cos %s \n' %(master_target, master_target, master_target))
		f.write('make_slc_tsx %s.xml %s.cos %s \n\n' %(slave_target, slave_target, slave_target))
		f.write('cd .. \n')
		f.write('p2p_TSX_SLC.csh %s %s config.tsx.txt' %(master_target, slave_target))
