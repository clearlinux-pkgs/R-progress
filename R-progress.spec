#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-progress
Version  : 1.2.2
Release  : 51
URL      : https://cran.r-project.org/src/contrib/progress_1.2.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/progress_1.2.2.tar.gz
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

%description
elapsed time, and/or the estimated completion time. They work in
    terminals, in 'Emacs' 'ESS', 'RStudio', 'Windows' 'Rgui' and the
    'macOS' 'R.app'. The package also provides a 'C++' 'API', that works
    with or without 'Rcpp'.

%prep
%setup -q -c -n progress
cd %{_builddir}/progress

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641079755

%install
export SOURCE_DATE_EPOCH=1641079755
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library progress
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library progress
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library progress
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc progress || :


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
