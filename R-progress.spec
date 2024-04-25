#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v3
# autospec commit: c1050fe
#
Name     : R-progress
Version  : 1.2.3
Release  : 54
URL      : https://cran.r-project.org/src/contrib/progress_1.2.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/progress_1.2.3.tar.gz
Summary  : Terminal Progress Bars
Group    : Development/Tools
License  : MIT
Requires: R-R6
Requires: R-crayon
Requires: R-hms
Requires: R-prettyunits
BuildRequires : R-R6
BuildRequires : R-crayon
BuildRequires : R-hms
BuildRequires : R-prettyunits
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
elapsed time, and/or the estimated completion time. They work in
    terminals, in 'Emacs' 'ESS', 'RStudio', 'Windows' 'Rgui' and the
    'macOS' 'R.app'. The package also provides a 'C++' 'API', that works
    with or without 'Rcpp'.

%prep
%setup -q -n progress
pushd ..
cp -a progress buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701910456

%install
export SOURCE_DATE_EPOCH=1701910456
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/progress/help/AnIndex
/usr/lib64/R/library/progress/help/aliases.rds
/usr/lib64/R/library/progress/help/figures/logo.png
/usr/lib64/R/library/progress/help/figures/logo.svg
/usr/lib64/R/library/progress/help/paths.rds
/usr/lib64/R/library/progress/help/progress.rdb
/usr/lib64/R/library/progress/help/progress.rdx
/usr/lib64/R/library/progress/html/00Index.html
/usr/lib64/R/library/progress/html/R.css
/usr/lib64/R/library/progress/include/RProgress.h
/usr/lib64/R/library/progress/tests/testthat.R
/usr/lib64/R/library/progress/tests/testthat/helper.R
/usr/lib64/R/library/progress/tests/testthat/progresstest/DESCRIPTION
/usr/lib64/R/library/progress/tests/testthat/progresstest/LICENSE
/usr/lib64/R/library/progress/tests/testthat/progresstest/NAMESPACE
/usr/lib64/R/library/progress/tests/testthat/progresstest/R/RcppExports.R
/usr/lib64/R/library/progress/tests/testthat/progresstest/R/test.R
/usr/lib64/R/library/progress/tests/testthat/progresstest/README.md
/usr/lib64/R/library/progress/tests/testthat/progresstest/src/RcppExports.cpp
/usr/lib64/R/library/progress/tests/testthat/progresstest/src/test.cpp
/usr/lib64/R/library/progress/tests/testthat/progresstest_1.0.0.tar.gz
/usr/lib64/R/library/progress/tests/testthat/test-cpp.R
/usr/lib64/R/library/progress/tests/testthat/test-progress.R
