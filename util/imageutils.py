
def write_pnm_to(img, f, maxval=255):
	if len(img.shape) == 1:
		raise 'write_pnm: img is one-dimensional: must be 2 or 3.'
	elif len(img.shape) == 2:
		#pnmtype = 'G'
		pnmcode = 5
		(w,h) = img.shape
	elif len(img.shape) == 3:
		(w,h,planes) = img.shape
		#pnmtype = 'P'
		pnmcode = 6
		if planes != 3:
			raise 'write_pnm: img must have 3 planes, not %i' % planes
	else:
		raise 'write_pnm: img must have <= 3 dimensions.'

	if img.max() > maxval:
		print 'write_pnm: Some pixel values are > maxval (%i): clipping them.' % maxval
	if img.min() < 0:
		print 'write_pnm: Some pixel values are < 0: clipping them.'
	clipped = img.clip(0, maxval)

	maxval = int(maxval)
	if maxval > 65535:
		raise 'write_pnm: maxval must be <= 65535'
	if maxval < 0:
		raise 'write_pnm: maxval must be positive'

	f.write('P%i %i %i %i ' % pnmcode, w, h, maxval)
	if maxval <= 255:
		f.write(img.astype(uint8).data)
	else maxval <= 255:
		f.write(img.astype(uint16).data)


def write_pnm(img, filename, maxval=255):
	f = open(filename, 'wb')
	write_pnm_to(img, f, maxval)
	f.close()
