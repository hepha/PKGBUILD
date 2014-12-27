#!/usr/bin/env python3
#
# This is a complex version of lilac.py for building
# a package from AUR.
#
# You can do something before/after building a package,
# including modify the 'pkgver' and 'md5sum' in PKBUILD.
#
# This is especially useful when a AUR package is
# out-of-date and you want to build a new one, or you
# want to build a package directly from sourceforge but
# using PKGBUILD from AUR.
#
# See also:
# [1] ruby-sass/lilac.py
# [2] aufs3-util-lily-git/lilac.py
# [3] octave-general/lilac.py
#

from lilaclib import *

build_prefix = 'extra-x86_64'
# depends = []

def pre_build():
  # obtain base PKGBUILD, e.g.
  aur_pre_build()

  for line in edit_file('PKGBUILD'):
    # edit PKGBUILD
    if 'install -dm755 "$pkgdir/usr/share/locale"' in line:
        print('  install -dm755 -g games "$pkgdir/${instdir}/lang/mo"')
    elif 'LOCALE_DIR="$pkgdir/usr/share/locale" lang/compile_mo.sh' in line:
        print('  LOCALE_DIR="$pkgdir/${instdir}/lang/mo" lang/compile_mo.sh')
    else:
        print(line)

def post_build():
  # do something after the package has successfully been built
  aur_post_build()

# do some cleanup here after building the package, regardless of result
# def post_build_always(success):
#   pass

if __name__ == '__main__':
  single_main()
