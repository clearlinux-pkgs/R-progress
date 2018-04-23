#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-progress
Version  : 1.1.2
Release  : 3
URL      : https://cran.r-project.org/src/contrib/progress_1.1.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/progress_1.1.2.tar.gz
Summary  : Terminal Progress Bars
Group    : Development/Tools
License  : MIT
Requires: R-prettyunits
BuildRequires : R-prettyunits
BuildRequires : clr-R-helpers

%description
elapsed time, and/or the estimated completion time. They work in
    terminals, in 'Emacs' 'ESS', 'RStudio', 'Windows' 'Rgui' and the
    'macOS' 'R.app'. The package also provides a 'C++' 'API', that works
    with or without 'Rcpp'.

%prep
%setup -q -c -n progress

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521269351

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521269351
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library progress
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library progress
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library progress
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library progress|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/progress/DESCRIPTION
/usr/lib64/R/library/progress/INDEX
/usr/lib64/R/library/progress/LICENSE
/usr/lib64/R/library/progress/Meta/Rd.rds
/usr/lib64/R/library/progress/Meta/features.rds
/usr/lib64/R/library/progress/Meta/hsearch.rds
/usr/lib64/R/library/progress/Meta/links.rds
/usr/lib64/R/library/progress/Meta/nsInfo.rds
/usr/lib64/R/library/progress/Meta/package.rds
/usr/lib64/R/library/progress/NAMESPACE
/usr/lib64/R/library/progress/NEWS.md
/usr/lib64/R/library/progress/R/progress
/usr/lib64/R/library/progress/R/progress.rdb
/usr/lib64/R/library/progress/R/progress.rdx
/usr/lib64/R/library/progress/README.metacran
/usr/lib64/R/library/progress/help/AnIndex
/usr/lib64/R/library/progress/help/aliases.rds
/usr/lib64/R/library/progress/help/paths.rds
/usr/lib64/R/library/progress/help/progress.rdb
/usr/lib64/R/library/progress/help/progress.rdx
/usr/lib64/R/library/progress/html/00Index.html
/usr/lib64/R/library/progress/html/R.css
/usr/lib64/R/library/progress/include/RProgress.h
/usr/lib64/R/library/progress/logo.png
/usr/lib64/R/library/progress/logo.svg
/usr/lib64/R/library/progress/progresstest/DESCRIPTION
/usr/lib64/R/library/progress/progresstest/LICENSE
/usr/lib64/R/library/progress/progresstest/NAMESPACE
/usr/lib64/R/library/progress/progresstest/R/RcppExports.R
/usr/lib64/R/library/progress/progresstest/R/test.R
/usr/lib64/R/library/progress/progresstest/README.md
/usr/lib64/R/library/progress/progresstest/src/RcppExports.cpp
/usr/lib64/R/library/progress/progresstest/src/test.cpp
