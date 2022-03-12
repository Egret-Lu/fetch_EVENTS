# FC= g77
FC= gfortran
FFLAGS= $(MYFFLAGS)
LFLAGS= $(MYLFLAGS)
# MYLIB= ~/Unix/libg77
# MYLIB= ~/Unix/lib
MYLIB= /Users/accardo/lib
#
PROG= idagrn6_mask
SUBS= spheroidal5.f toroidal5.f spheroidal_exc5.f toroidal_exc5.f \
      curse4.f source_strains5.f cubic.f zfcns.f load_tables.f dwdd_h.f \
      readint_h.f load_crust20.f load_kern_c51.f avg_crust20.f avg_dbdb5.f \
      dwdd_c51.f dwdd_db.f

OBJS= $(PROG).o $(SUBS:.f=.o)

.f.o:
	$(FC) $(FFLAGS) -c $*.f

#----------------------------------------------------------------------------------

$(PROG): $(OBJS) 
	$(FC) $(FFLAGS) $(LFLAGS) -o $(MYBIN)/$@ $(OBJS) \
	$(MYLIB)/libcip.a \
	/usr/local/sac/lib/sacio.a \
	$(MYLIB)/libharm.a \
	$(MYLIB)/libutil.a

# check object files for dependency on .h files
$(OBJS): parameter5.h
	$(FC) $(FFLAGS) -c $*.f
