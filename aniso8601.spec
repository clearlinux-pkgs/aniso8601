#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : aniso8601
Version  : 8.0.0
Release  : 13
URL      : https://files.pythonhosted.org/packages/2f/45/f2aec388115ea65a2b95b3dc1ba058a8470675fe16bcd4678a44a59776ea/aniso8601-8.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/2f/45/f2aec388115ea65a2b95b3dc1ba058a8470675fe16bcd4678a44a59776ea/aniso8601-8.0.0.tar.gz
Summary  : A library for parsing ISO 8601 strings.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: aniso8601-license = %{version}-%{release}
Requires: aniso8601-python = %{version}-%{release}
Requires: aniso8601-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : python-dateutil

%description
aniso8601
=========

Another ISO 8601 parser for Python
----------------------------------

Features
========
* Pure Python implementation
* Python 3 support
* Logical behavior

  - Parse a time, get a `datetime.time <http://docs.python.org/2/library/datetime.html#datetime.time>`_
  - Parse a date, get a `datetime.date <http://docs.python.org/2/library/datetime.html#datetime.date>`_
  - Parse a datetime, get a `datetime.datetime <http://docs.python.org/2/library/datetime.html#datetime.datetime>`_
  - Parse a duration, get a `datetime.timedelta <http://docs.python.org/2/library/datetime.html#datetime.timedelta>`_
  - Parse an interval, get a tuple of dates or datetimes
  - Parse a repeating interval, get a date or datetime `generator <http://www.python.org/dev/peps/pep-0255/>`_

* UTC offset represented as fixed-offset tzinfo
* Parser separate from representation, allowing parsing to different datetime formats
* No regular expressions

Installation
============

The recommended installation method is to use pip::

  $ pip install aniso8601

Alternatively, you can download the source (git repository hosted at `Bitbucket <https://bitbucket.org/nielsenb/aniso8601>`_) and install directly::

  $ python setup.py install

Use
===

Parsing datetimes
-----------------

To parse a typical ISO 8601 datetime string::

  >>> import aniso8601
  >>> aniso8601.parse_datetime('1977-06-10T12:00:00Z')
  datetime.datetime(1977, 6, 10, 12, 0, tzinfo=+0:00:00 UTC)

Alternative delimiters can be specified, for example, a space::

  >>> aniso8601.parse_datetime('1977-06-10 12:00:00Z', delimiter=' ')
  datetime.datetime(1977, 6, 10, 12, 0, tzinfo=+0:00:00 UTC)

UTC offsets are supported::

  >>> aniso8601.parse_datetime('1979-06-05T08:00:00-08:00')
  datetime.datetime(1979, 6, 5, 8, 0, tzinfo=-8:00:00 UTC)

If a UTC offset is not specified, the returned datetime will be naive::

  >>> aniso8601.parse_datetime('1983-01-22T08:00:00')
  datetime.datetime(1983, 1, 22, 8, 0)

Leap seconds are currently not supported and attempting to parse one raises a :code:`LeapSecondError`::

  >>> aniso8601.parse_datetime('2018-03-06T23:59:60')
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "aniso8601/time.py", line 131, in parse_datetime
      return builder.build_datetime(datepart, timepart)
    File "aniso8601/builder.py", line 300, in build_datetime
      cls._build_object(time))
    File "aniso8601/builder.py", line 71, in _build_object
      ss=parsetuple[2], tz=parsetuple[3])
    File "aniso8601/builder.py", line 253, in build_time
      raise LeapSecondError('Leap seconds are not supported.')
  aniso8601.exceptions.LeapSecondError: Leap seconds are not supported.

Parsing dates
-------------

To parse a date represented in an ISO 8601 string::

  >>> import aniso8601
  >>> aniso8601.parse_date('1984-04-23')
  datetime.date(1984, 4, 23)

Basic format is supported as well::

  >>> aniso8601.parse_date('19840423')
  datetime.date(1984, 4, 23)

To parse a date using the ISO 8601 week date format::

  >>> aniso8601.parse_date('1986-W38-1')
  datetime.date(1986, 9, 15)

To parse an ISO 8601 ordinal date::

  >>> aniso8601.parse_date('1988-132')
  datetime.date(1988, 5, 11)

Parsing times
-------------

To parse a time formatted as an ISO 8601 string::

  >>> import aniso8601
  >>> aniso8601.parse_time('11:31:14')
  datetime.time(11, 31, 14)

As with all of the above, basic format is supported::

  >>> aniso8601.parse_time('113114')
  datetime.time(11, 31, 14)

A UTC offset can be specified for times::

  >>> aniso8601.parse_time('17:18:19-02:30')
  datetime.time(17, 18, 19, tzinfo=-2:30:00 UTC)
  >>> aniso8601.parse_time('171819Z')
  datetime.time(17, 18, 19, tzinfo=+0:00:00 UTC)

Reduced accuracy is supported::

  >>> aniso8601.parse_time('21:42')
  datetime.time(21, 42)
  >>> aniso8601.parse_time('22')
  datetime.time(22, 0)

A decimal fraction is always allowed on the lowest order element of an ISO 8601 formatted time::

  >>> aniso8601.parse_time('22:33.5')
  datetime.time(22, 33, 30)
  >>> aniso8601.parse_time('23.75')
  datetime.time(23, 45)

The decimal fraction can be specified with a comma instead of a full-stop::

  >>> aniso8601.parse_time('22:33,5')
  datetime.time(22, 33, 30)
  >>> aniso8601.parse_time('23,75')
  datetime.time(23, 45)

Leap seconds are currently not supported and attempting to parse one raises a :code:`LeapSecondError`::

  >>> aniso8601.parse_time('23:59:60')
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "aniso8601/time.py", line 116, in parse_time
      return _RESOLUTION_MAP[get_time_resolution(timestr)](timestr, tz, builder)
    File "aniso8601/time.py", line 165, in _parse_second_time
      return builder.build_time(hh=hourstr, mm=minutestr, ss=secondstr, tz=tz)
    File "aniso8601/builder.py", line 253, in build_time
      raise LeapSecondError('Leap seconds are not supported.')
  aniso8601.exceptions.LeapSecondError: Leap seconds are not supported.

Parsing durations
-----------------

To parse a duration formatted as an ISO 8601 string::

  >>> import aniso8601
  >>> aniso8601.parse_duration('P1Y2M3DT4H54M6S')
  datetime.timedelta(428, 17646)

Reduced accuracy is supported::

  >>> aniso8601.parse_duration('P1Y')
  datetime.timedelta(365)

A decimal fraction is allowed on the lowest order element::

  >>> aniso8601.parse_duration('P1YT3.5M')
  datetime.timedelta(365, 210)

The decimal fraction can be specified with a comma instead of a full-stop::

  >>> aniso8601.parse_duration('P1YT3,5M')
  datetime.timedelta(365, 210)

Parsing a duration from a combined date and time is supported as well::

  >>> aniso8601.parse_duration('P0001-01-02T01:30:5')
  datetime.timedelta(397, 5405)

Parsing intervals
-----------------

To parse an interval specified by a start and end::

  >>> import aniso8601
  >>> aniso8601.parse_interval('2007-03-01T13:00:00/2008-05-11T15:30:00')
  (datetime.datetime(2007, 3, 1, 13, 0), datetime.datetime(2008, 5, 11, 15, 30))

Intervals specified by a start time and a duration are supported::

  >>> aniso8601.parse_interval('2007-03-01T13:00:00Z/P1Y2M10DT2H30M')
  (datetime.datetime(2007, 3, 1, 13, 0, tzinfo=+0:00:00 UTC), datetime.datetime(2008, 5, 9, 15, 30, tzinfo=+0:00:00 UTC))

A duration can also be specified by a duration and end time::

  >>> aniso8601.parse_interval('P1M/1981-04-05')
  (datetime.date(1981, 4, 5), datetime.date(1981, 3, 6))

Notice that the result of the above parse is not in order from earliest to latest. If sorted intervals are required, simply use the :code:`sorted` keyword as shown below::

  >>> sorted(aniso8601.parse_interval('P1M/1981-04-05'))
  [datetime.date(1981, 3, 6), datetime.date(1981, 4, 5)]

The end of an interval is returned as a datetime when required to maintain the resolution specified by a duration, even if the duration start is given as a date::

  >>> aniso8601.parse_interval('2014-11-12/PT4H54M6.5S')
  (datetime.date(2014, 11, 12), datetime.datetime(2014, 11, 12, 4, 54, 6, 500000))
  >>> aniso8601.parse_interval('2007-03-01/P1.5D')
  (datetime.date(2007, 3, 1), datetime.datetime(2007, 3, 2, 12, 0))

Repeating intervals are supported as well, and return a generator::

  >>> aniso8601.parse_repeating_interval('R3/1981-04-05/P1D')
  <generator object _date_generator at 0x7fd800d3b320>
  >>> list(aniso8601.parse_repeating_interval('R3/1981-04-05/P1D'))
  [datetime.date(1981, 4, 5), datetime.date(1981, 4, 6), datetime.date(1981, 4, 7)]

Repeating intervals are allowed to go in the reverse direction::

  >>> list(aniso8601.parse_repeating_interval('R2/PT1H2M/1980-03-05T01:01:00'))
  [datetime.datetime(1980, 3, 5, 1, 1), datetime.datetime(1980, 3, 4, 23, 59)]

Unbounded intervals are also allowed (Python 2)::

  >>> result = aniso8601.parse_repeating_interval('R/PT1H2M/1980-03-05T01:01:00')
  >>> result.next()
  datetime.datetime(1980, 3, 5, 1, 1)
  >>> result.next()
  datetime.datetime(1980, 3, 4, 23, 59)

or for Python 3::

  >>> result = aniso8601.parse_repeating_interval('R/PT1H2M/1980-03-05T01:01:00')
  >>> next(result)
  datetime.datetime(1980, 3, 5, 1, 1)
  >>> next(result)
  datetime.datetime(1980, 3, 4, 23, 59)

Note that you should never try to convert a generator produced by an unbounded interval to a list::

  >>> list(aniso8601.parse_repeating_interval('R/PT1H2M/1980-03-05T01:01:00'))
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "aniso8601/builders/python.py", line 463, in _date_generator_unbounded
      currentdate += timedelta
  OverflowError: date value out of range

Date and time resolution
------------------------

In some situations, it may be useful to figure out the resolution provided by an ISO 8601 date or time string. Two functions are provided for this purpose.

To get the resolution of a ISO 8601 time string::

  >>> aniso8601.get_time_resolution('11:31:14') == aniso8601.resolution.TimeResolution.Seconds
  True
  >>> aniso8601.get_time_resolution('11:31') == aniso8601.resolution.TimeResolution.Minutes
  True
  >>> aniso8601.get_time_resolution('11') == aniso8601.resolution.TimeResolution.Hours
  True

Similarly, for an ISO 8601 date string::

  >>> aniso8601.get_date_resolution('1981-04-05') == aniso8601.resolution.DateResolution.Day
  True
  >>> aniso8601.get_date_resolution('1981-04') == aniso8601.resolution.DateResolution.Month
  True
  >>> aniso8601.get_date_resolution('1981') == aniso8601.resolution.DateResolution.Year
  True

Builders
========

Builders can be used to change the output format of a parse operation. All parse functions have a :code:`builder` keyword argument which accepts a builder class.

Two builders are included. The :code:`PythonTimeBuilder` (the default) in the  :code:`aniso8601.builders.python` module, and the :code:`TupleBuilder` which returns the parse result as a tuple of strings and is located in the :code:`aniso8601.builders` module.

The following builders are available as separate projects:

* `RelativeTimeBuilder <https://bitbucket.org/nielsenb/relativetimebuilder>`_ supports parsing to `datetutil relativedelta types <https://dateutil.readthedocs.io/en/stable/relativedelta.html>`_ for calendar level accuracy
* `AttoTimeBuilder <https://bitbucket.org/nielsenb/attotimebuilder>`_ supports parsing directly to `attotime attodatetime and attotimedelta types <https://bitbucket.org/nielsenb/attotime>`_ which support sub-nanosecond precision
* `NumPyTimeBuilder <https://bitbucket.org/nielsenb/numpytimebuilder>`_ supports parsing directly to `NumPy datetime64 and timedelta64 types <https://docs.scipy.org/doc/numpy/reference/arrays.datetime.html>`_

TupleBuilder
------------

The :code:`TupleBuilder` returns parse results as tuples of strings. It is located in the :code:`aniso8601.builders` module.

Datetimes
^^^^^^^^^

Parsing a datetime returns a tuple containing a date tuple as a collection of strings, a time tuple as a collection of strings, and the 'datetime' string. The date tuple contains the following parse components: :code:`(YYYY, MM, DD, Www, D, DDD, 'date')`. The time tuple contains the following parse components :code:`(hh, mm, ss, tz, 'time')`, where :code:`tz` is a tuple with the following components :code:`(negative, Z, hh, mm, name, 'timezone')` with :code:`negative` and :code:`Z` being booleans::

  >>> import aniso8601
  >>> from aniso8601.builders import TupleBuilder
  >>> aniso8601.parse_datetime('1977-06-10T12:00:00', builder=TupleBuilder)
  (('1977', '06', '10', None, None, None, 'date'), ('12', '00', '00', None, 'time'), 'datetime')
  >>> aniso8601.parse_datetime('1979-06-05T08:00:00-08:00', builder=TupleBuilder)
  (('1979', '06', '05', None, None, None, 'date'), ('08', '00', '00', (True, None, '08', '00', '-08:00', 'timezone'), 'time'), 'datetime')

Dates
^^^^^

Parsing a date returns a tuple containing the following parse components: :code:`(YYYY, MM, DD, Www, D, DDD, 'date')`::

  >>> import aniso8601
  >>> from aniso8601.builders import TupleBuilder
  >>> aniso8601.parse_date('1984-04-23', builder=TupleBuilder)
  ('1984', '04', '23', None, None, None, 'date')
  >>> aniso8601.parse_date('1986-W38-1', builder=TupleBuilder)
  ('1986', None, None, '38', '1', None, 'date')
  >>> aniso8601.parse_date('1988-132', builder=TupleBuilder)
  ('1988', None, None, None, None, '132', 'date')

Times
^^^^^

Parsing a time returns a tuple containing following parse components: :code:`(hh, mm, ss, tz, 'time')`, where :code:`tz` is a tuple with the following components :code:`(negative, Z, hh, mm, name, 'timezone')` with :code:`negative` and :code:`Z` being booleans::

  >>> import aniso8601
  >>> from aniso8601.builders import TupleBuilder
  >>> aniso8601.parse_time('11:31:14', builder=TupleBuilder)
  ('11', '31', '14', None, 'time')
  >>> aniso8601.parse_time('171819Z', builder=TupleBuilder)
  ('17', '18', '19', (False, True, None, None, 'Z', 'timezone'), 'time')
  >>> aniso8601.parse_time('17:18:19-02:30', builder=TupleBuilder)
  ('17', '18', '19', (True, None, '02', '30', '-02:30', 'timezone'), 'time')

Durations
^^^^^^^^^

Parsing a duration returns a tuple containing the following parse components: :code:`(PnY, PnM, PnW, PnD, TnH, TnM, TnS, 'duration')`::

  >>> import aniso8601
  >>> from aniso8601.builders import TupleBuilder
  >>> aniso8601.parse_duration('P1Y2M3DT4H54M6S', builder=TupleBuilder)
  ('1', '2', None, '3', '4', '54', '6', 'duration')
  >>> aniso8601.parse_duration('P7W', builder=TupleBuilder)
  (None, None, '7', None, None, None, None, 'duration')

Intervals
^^^^^^^^^

Parsing an interval returns a tuple containing the following parse components: :code:`(start, end, duration, 'interval')`, :code:`start` and :code:`end` may both be datetime or date tuples, :code:`duration` is a duration tuple::

  >>> import aniso8601
  >>> from aniso8601.builders import TupleBuilder
  >>> aniso8601.parse_interval('2007-03-01T13:00:00/2008-05-11T15:30:00', builder=TupleBuilder)
  ((('2007', '03', '01', None, None, None, 'date'), ('13', '00', '00', None, 'time'), 'datetime'), (('2008', '05', '11', None, None, None, 'date'), ('15', '30', '00', None, 'time'), 'datetime'), None, 'interval')
  >>> aniso8601.parse_interval('2007-03-01T13:00:00Z/P1Y2M10DT2H30M', builder=TupleBuilder)
  ((('2007', '03', '01', None, None, None, 'date'), ('13', '00', '00', (False, True, None, None, 'Z', 'timezone'), 'time'), 'datetime'), None, ('1', '2', None, '10', '2', '30', None, 'duration'), 'interval')
  >>> aniso8601.parse_interval('P1M/1981-04-05', builder=TupleBuilder)
  (None, ('1981', '04', '05', None, None, None, 'date'), (None, '1', None, None, None, None, None, 'duration'), 'interval')

A repeating interval returns a tuple containing the following parse components: :code:`(R, Rnn, interval, 'repeatinginterval')` where :code:`R` is a boolean, :code:`True` for an unbounded interval, :code:`False` otherwise.::

  >>> aniso8601.parse_repeating_interval('R3/1981-04-05/P1D', builder=TupleBuilder)
  (False, '3', (('1981', '04', '05', None, None, None, 'date'), None, (None, None, None, '1', None, None, None, 'duration'), 'interval'), 'repeatinginterval')
  >>> aniso8601.parse_repeating_interval('R/PT1H2M/1980-03-05T01:01:00', builder=TupleBuilder)
  (True, None, (None, (('1980', '03', '05', None, None, None, 'date'), ('01', '01', '00', None, 'time'), 'datetime'), (None, None, None, None, '1', '2', None, 'duration'), 'interval'), 'repeatinginterval')

Development
===========

Setup
-----

It is recommended to develop using a `virtualenv <https://virtualenv.pypa.io/en/stable/>`_.

Tests
-----

Tests can be run using `setuptools <https://setuptools.readthedocs.io/en/latest/setuptools.html>`::

   $ python setup.py test

Contributing
============

aniso8601 is an open source project hosted on `Bitbucket <https://bitbucket.org/nielsenb/aniso8601>`_.

Any and all bugs are welcome on our `issue tracker <https://bitbucket.org/nielsenb/aniso8601/issues>`_.
Of particular interest are valid ISO 8601 strings that don't parse, or invalid ones that do. At a minimum,
bug reports should include an example of the misbehaving string, as well as the expected result. Of course
patches containing unit tests (or fixed bugs) are welcome!

References
==========

* `ISO 8601:2004(E) <http://dotat.at/tmp/ISO_8601-2004_E.pdf>`_ (Caution, PDF link)
* `Wikipedia article on ISO 8601 <http://en.wikipedia.org/wiki/Iso8601>`_
* `Discussion on alternative ISO 8601 parsers for Python <https://groups.google.com/forum/#!topic/comp.lang.python/Q2w4R89Nq1w>`_

%package license
Summary: license components for the aniso8601 package.
Group: Default

%description license
license components for the aniso8601 package.


%package python
Summary: python components for the aniso8601 package.
Group: Default
Requires: aniso8601-python3 = %{version}-%{release}

%description python
python components for the aniso8601 package.


%package python3
Summary: python3 components for the aniso8601 package.
Group: Default
Requires: python3-core
Provides: pypi(aniso8601)

%description python3
python3 components for the aniso8601 package.


%prep
%setup -q -n aniso8601-8.0.0
cd %{_builddir}/aniso8601-8.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582845538
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/aniso8601
cp %{_builddir}/aniso8601-8.0.0/LICENSE %{buildroot}/usr/share/package-licenses/aniso8601/c0ef2a5ffbd27ad067d3ff3ad41dd4aa02d021c8
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/aniso8601/c0ef2a5ffbd27ad067d3ff3ad41dd4aa02d021c8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
