#!/usr/bin/env python
# Copyright 2012 Cloudera Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This is a list of all the functions that are not auto-generated.
# It contains all the meta data that describes the function.
templated_type_symbol_map = {
  'bool'      : 'b',
  'int8_t'    : 'a',
  'int16_t'   : 's',
  'int32_t'   : 'i',
  'int64_t'   : 'l',
  'float'     : 'f',
  'double'    : 'd',
  'string'    : 'NS_11StringValueE',
  'timestamp' : 'NS_14TimestampValueE'
}

# Generates the BE symbol for the Compute Function class_name::fn_name<templated_type>.
# Does not handle varargs.
# TODO: this is a stopgap. ComputeFunctions are being removed and we can use the
# symbol lookup code in the BE.
def symbol(class_name, fn_name, templated_type = None):
  sym = '_ZN6impala'
  sym += str(len(class_name)) + class_name
  sym += str(len(fn_name)) + fn_name
  if templated_type == None:
    sym += 'EPNS_4ExprEPNS_8TupleRowE'
  else:
    sym += 'I'
    sym += templated_type_symbol_map[templated_type]
    sym += 'EEPvPNS_4ExprEPNS_8TupleRowE'
  return sym

# The format is:
#   [sql aliases], <return_type>, [<args>], <backend symbol>,
# With an optional
#   <prepare symbol>, <close symbol>
#
# 'sql aliases' are the function names that can be used from sql. There must be at least
# one per function.
#
# The symbol can be empty for functions that are not yet implemented or are special-cased
# in Expr::CreateExpr() (i.e., functions that are implemented via a custom Expr class
# rather than a single function).
functions = [
  [['udf_pi'], 'DOUBLE', [], 'impala::UdfBuiltins::Pi'],
  [['udf_abs'], 'DOUBLE', ['DOUBLE'], 'impala::UdfBuiltins::Abs'],
  [['udf_lower'], 'STRING', ['STRING'], 'impala::UdfBuiltins::Lower'],
  [['max_int'], 'INT', [],
   '_ZN6impala11UdfBuiltins6MaxIntEPN10impala_udf15FunctionContextE'],
  [['max_tinyint'], 'TINYINT', [],
   '_ZN6impala11UdfBuiltins10MaxTinyIntEPN10impala_udf15FunctionContextE'],
  [['max_smallint'], 'SMALLINT', [],
   '_ZN6impala11UdfBuiltins11MaxSmallIntEPN10impala_udf15FunctionContextE'],
  [['max_bigint'], 'BIGINT', [],
   '_ZN6impala11UdfBuiltins9MaxBigIntEPN10impala_udf15FunctionContextE'],
  [['min_int'], 'INT', [],
   '_ZN6impala11UdfBuiltins6MinIntEPN10impala_udf15FunctionContextE'],
  [['min_tinyint'], 'TINYINT', [],
   '_ZN6impala11UdfBuiltins10MinTinyIntEPN10impala_udf15FunctionContextE'],
  [['min_smallint'], 'SMALLINT', [],
   '_ZN6impala11UdfBuiltins11MinSmallIntEPN10impala_udf15FunctionContextE'],
  [['min_bigint'], 'BIGINT', [],
   '_ZN6impala11UdfBuiltins9MinBigIntEPN10impala_udf15FunctionContextE'],
  [['is_nan'], 'BOOLEAN', ['DOUBLE'],
   '_ZN6impala11UdfBuiltins5IsNanEPN10impala_udf15FunctionContextERKNS1_9DoubleValE'],
  [['is_inf'], 'BOOLEAN', ['DOUBLE'],
   '_ZN6impala11UdfBuiltins5IsInfEPN10impala_udf15FunctionContextERKNS1_9DoubleValE'],
  [['trunc'], 'TIMESTAMP', ['TIMESTAMP', 'STRING'],
   '_ZN6impala11UdfBuiltins5TruncEPN10impala_udf15FunctionContextERKNS1_12TimestampValERKNS1_9StringValE',
   '_ZN6impala11UdfBuiltins12TruncPrepareEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE',
   '_ZN6impala11UdfBuiltins10TruncCloseEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE'],
  # Don't add an entry for EXTRACT(STRING, TIMESTAMP). STRINGs may be used to represent
  # TIMESTAMPs meaning EXTRACT(STRING, STRING) is valid. If EXTRACT(STRING, TIMESTAMP)
  # is added, it takes precedence over the existing EXTRACT(TIMESTAMP, STRING)
  # which could break users.
  [['extract'], 'INT', ['TIMESTAMP', 'STRING'],
   '_ZN6impala11UdfBuiltins7ExtractEPN10impala_udf15FunctionContextERKNS1_12TimestampValERKNS1_9StringValE',
   '_ZN6impala11UdfBuiltins21SwappedExtractPrepareEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE',
   '_ZN6impala11UdfBuiltins12ExtractCloseEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE'],
  [['date_part'], 'INT', ['STRING', 'TIMESTAMP'],
   '_ZN6impala11UdfBuiltins7ExtractEPN10impala_udf15FunctionContextERKNS1_9StringValERKNS1_12TimestampValE',
   '_ZN6impala11UdfBuiltins14ExtractPrepareEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE',
   '_ZN6impala11UdfBuiltins12ExtractCloseEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE'],

  [['madlib_encode_vector'], 'STRING', ['STRING'],
    '_ZN6impala11UdfBuiltins12EncodeVectorEPN10impala_udf15FunctionContextERKNS1_9StringValE'],
  [['madlib_decode_vector'], 'STRING', ['STRING'],
    '_ZN6impala11UdfBuiltins12DecodeVectorEPN10impala_udf15FunctionContextERKNS1_9StringValE'],
  [['madlib_print_vector'], 'STRING', ['STRING'],
    '_ZN6impala11UdfBuiltins11PrintVectorEPN10impala_udf15FunctionContextERKNS1_9StringValE'],
  [['madlib_vector'], 'STRING', ['DOUBLE', '...'],
    '_ZN6impala11UdfBuiltins8ToVectorEPN10impala_udf15FunctionContextEiPKNS1_9DoubleValE'],
  [['madlib_vector_get'], 'DOUBLE', ['BIGINT', 'STRING'],
    '_ZN6impala11UdfBuiltins9VectorGetEPN10impala_udf15FunctionContextERKNS1_9BigIntValERKNS1_9StringValE'],

  # Timestamp functions
  [['unix_timestamp'], 'INT', ['STRING'], '_ZN6impala18TimestampFunctions14UnixFromStringEPN10impala_udf15FunctionContextERKNS1_9StringValE'],
  [['year'], 'INT', ['TIMESTAMP'], '_ZN6impala18TimestampFunctions4YearEPN10impala_udf15FunctionContextERKNS1_12TimestampValE'],
  [['month'], 'INT', ['TIMESTAMP'], '_ZN6impala18TimestampFunctions5MonthEPN10impala_udf15FunctionContextERKNS1_12TimestampValE'],
  [['dayofweek'], 'INT', ['TIMESTAMP'], '_ZN6impala18TimestampFunctions9DayOfWeekEPN10impala_udf15FunctionContextERKNS1_12TimestampValE'],
  [['day', 'dayofmonth'], 'INT', ['TIMESTAMP'], '_ZN6impala18TimestampFunctions10DayOfMonthEPN10impala_udf15FunctionContextERKNS1_12TimestampValE'],
  [['dayofyear'], 'INT', ['TIMESTAMP'], '_ZN6impala18TimestampFunctions9DayOfYearEPN10impala_udf15FunctionContextERKNS1_12TimestampValE'],
  [['weekofyear'], 'INT', ['TIMESTAMP'], '_ZN6impala18TimestampFunctions10WeekOfYearEPN10impala_udf15FunctionContextERKNS1_12TimestampValE'],
  [['hour'], 'INT', ['TIMESTAMP'], '_ZN6impala18TimestampFunctions4HourEPN10impala_udf15FunctionContextERKNS1_12TimestampValE'],
  [['minute'], 'INT', ['TIMESTAMP'], '_ZN6impala18TimestampFunctions6MinuteEPN10impala_udf15FunctionContextERKNS1_12TimestampValE'],
  [['second'], 'INT', ['TIMESTAMP'], '_ZN6impala18TimestampFunctions6SecondEPN10impala_udf15FunctionContextERKNS1_12TimestampValE'],
  [['to_date'], 'STRING', ['TIMESTAMP'], '_ZN6impala18TimestampFunctions6ToDateEPN10impala_udf15FunctionContextERKNS1_12TimestampValE'],
  [['dayname'], 'STRING', ['TIMESTAMP'], '_ZN6impala18TimestampFunctions7DayNameEPN10impala_udf15FunctionContextERKNS1_12TimestampValE'],
  [['years_add'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb1EN10impala_udf6IntValEN5boost9date_time14years_durationINS4_9gregorian21greg_durations_configEEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['years_add'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb1EN10impala_udf9BigIntValEN5boost9date_time14years_durationINS4_9gregorian21greg_durations_configEEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['years_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb0EN10impala_udf6IntValEN5boost9date_time14years_durationINS4_9gregorian21greg_durations_configEEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['years_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb0EN10impala_udf9BigIntValEN5boost9date_time14years_durationINS4_9gregorian21greg_durations_configEEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['months_add', 'add_months'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb1EN10impala_udf6IntValEN5boost9date_time15months_durationINS4_9gregorian21greg_durations_configEEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['months_add', 'add_months'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb1EN10impala_udf9BigIntValEN5boost9date_time15months_durationINS4_9gregorian21greg_durations_configEEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['months_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb0EN10impala_udf6IntValEN5boost9date_time15months_durationINS4_9gregorian21greg_durations_configEEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['months_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb0EN10impala_udf9BigIntValEN5boost9date_time15months_durationINS4_9gregorian21greg_durations_configEEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['weeks_add'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb1EN10impala_udf6IntValEN5boost9gregorian14weeks_durationEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['weeks_add'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb1EN10impala_udf9BigIntValEN5boost9gregorian14weeks_durationEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['weeks_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb0EN10impala_udf6IntValEN5boost9gregorian14weeks_durationEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['weeks_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb0EN10impala_udf9BigIntValEN5boost9gregorian14weeks_durationEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['days_add', 'date_add', 'adddate'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb1EN10impala_udf6IntValEN5boost9gregorian13date_durationEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['days_add', 'date_add', 'adddate'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb1EN10impala_udf9BigIntValEN5boost9gregorian13date_durationEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['days_sub', 'date_sub', 'subdate'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb0EN10impala_udf6IntValEN5boost9gregorian13date_durationEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['days_sub', 'date_sub', 'subdate'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb0EN10impala_udf9BigIntValEN5boost9gregorian13date_durationEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['hours_add'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EN10impala_udf6IntValEN5boost10posix_time5hoursEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['hours_add'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EN10impala_udf9BigIntValEN5boost10posix_time5hoursEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['hours_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EN10impala_udf6IntValEN5boost10posix_time5hoursEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['hours_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EN10impala_udf9BigIntValEN5boost10posix_time5hoursEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['minutes_add'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EN10impala_udf6IntValEN5boost10posix_time7minutesEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['minutes_add'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EN10impala_udf9BigIntValEN5boost10posix_time7minutesEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['minutes_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EN10impala_udf6IntValEN5boost10posix_time7minutesEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['minutes_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EN10impala_udf9BigIntValEN5boost10posix_time7minutesEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['seconds_add'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EN10impala_udf6IntValEN5boost10posix_time7secondsEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['seconds_add'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EN10impala_udf9BigIntValEN5boost10posix_time7secondsEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['seconds_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EN10impala_udf6IntValEN5boost10posix_time7secondsEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['seconds_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EN10impala_udf9BigIntValEN5boost10posix_time7secondsEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['milliseconds_add'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EN10impala_udf6IntValEN5boost9date_time18subsecond_durationINS4_10posix_time13time_durationELl1000EEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['milliseconds_add'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EN10impala_udf9BigIntValEN5boost9date_time18subsecond_durationINS4_10posix_time13time_durationELl1000EEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['milliseconds_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EN10impala_udf6IntValEN5boost9date_time18subsecond_durationINS4_10posix_time13time_durationELl1000EEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['milliseconds_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EN10impala_udf9BigIntValEN5boost9date_time18subsecond_durationINS4_10posix_time13time_durationELl1000EEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['microseconds_add'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EN10impala_udf6IntValEN5boost9date_time18subsecond_durationINS4_10posix_time13time_durationELl1000000EEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['microseconds_add'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EN10impala_udf9BigIntValEN5boost9date_time18subsecond_durationINS4_10posix_time13time_durationELl1000000EEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['microseconds_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EN10impala_udf6IntValEN5boost9date_time18subsecond_durationINS4_10posix_time13time_durationELl1000000EEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['microseconds_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EN10impala_udf9BigIntValEN5boost9date_time18subsecond_durationINS4_10posix_time13time_durationELl1000000EEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['nanoseconds_add'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EN10impala_udf6IntValEN5boost9date_time18subsecond_durationINS4_10posix_time13time_durationELl1000000000EEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['nanoseconds_add'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EN10impala_udf9BigIntValEN5boost9date_time18subsecond_durationINS4_10posix_time13time_durationELl1000000000EEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['nanoseconds_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EN10impala_udf6IntValEN5boost9date_time18subsecond_durationINS4_10posix_time13time_durationELl1000000000EEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['nanoseconds_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EN10impala_udf9BigIntValEN5boost9date_time18subsecond_durationINS4_10posix_time13time_durationELl1000000000EEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['datediff'], 'INT', ['TIMESTAMP', 'TIMESTAMP'], '_ZN6impala18TimestampFunctions8DateDiffEPN10impala_udf15FunctionContextERKNS1_12TimestampValES6_'],
   [['unix_timestamp'], 'INT', [], '_ZN6impala18TimestampFunctions4UnixEPN10impala_udf15FunctionContextE'],
  [['unix_timestamp'], 'INT', ['TIMESTAMP'], '_ZN6impala18TimestampFunctions4UnixEPN10impala_udf15FunctionContextERKNS1_12TimestampValE'],
  [['unix_timestamp'], 'INT', ['STRING', 'STRING'], '_ZN6impala18TimestampFunctions4UnixEPN10impala_udf15FunctionContextERKNS1_9StringValES6_',
          '_ZN6impala18TimestampFunctions22UnixAndFromUnixPrepareEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE',
          '_ZN6impala18TimestampFunctions20UnixAndFromUnixCloseEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE'],
  [['from_unixtime'], 'STRING', ['INT'],
      '_ZN6impala18TimestampFunctions8FromUnixIN10impala_udf6IntValEEENS2_9StringValEPNS2_15FunctionContextERKT_'],
  [['from_unixtime'], 'STRING', ['INT', 'STRING'],
      '_ZN6impala18TimestampFunctions8FromUnixIN10impala_udf6IntValEEENS2_9StringValEPNS2_15FunctionContextERKT_RKS4_',
      '_ZN6impala18TimestampFunctions22UnixAndFromUnixPrepareEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE',
     '_ZN6impala18TimestampFunctions20UnixAndFromUnixCloseEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE'],
  [['from_unixtime'], 'STRING', ['BIGINT'],
      '_ZN6impala18TimestampFunctions8FromUnixIN10impala_udf9BigIntValEEENS2_9StringValEPNS2_15FunctionContextERKT_'],
  [['from_unixtime'], 'STRING', ['BIGINT', 'STRING'],
      '_ZN6impala18TimestampFunctions8FromUnixIN10impala_udf9BigIntValEEENS2_9StringValEPNS2_15FunctionContextERKT_RKS4_',
      '_ZN6impala18TimestampFunctions22UnixAndFromUnixPrepareEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE',
      '_ZN6impala18TimestampFunctions20UnixAndFromUnixCloseEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE'],
  [['now', 'current_timestamp'], 'TIMESTAMP', [], '_ZN6impala18TimestampFunctions3NowEPN10impala_udf15FunctionContextE'],
  [['from_utc_timestamp'], 'TIMESTAMP', ['TIMESTAMP', 'STRING'],
   "impala::TimestampFunctions::FromUtc"],
  [['to_utc_timestamp'], 'TIMESTAMP', ['TIMESTAMP', 'STRING'],
   "impala::TimestampFunctions::ToUtc"],

  # Math builtin functions
  [['pi'], 'DOUBLE', [], 'impala::MathFunctions::Pi'],
  [['e'], 'DOUBLE', [], 'impala::MathFunctions::E'],
  [['abs'], 'BIGINT', ['BIGINT'], 'impala::MathFunctions::Abs'],
  [['abs'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Abs'],
  [['abs'], 'FLOAT', ['FLOAT'], 'impala::MathFunctions::Abs'],
  [['abs'], 'INT', ['INT'], 'impala::MathFunctions::Abs'],
  [['abs'], 'SMALLINT', ['SMALLINT'], 'impala::MathFunctions::Abs'],
  [['abs'], 'TINYINT', ['TINYINT'], 'impala::MathFunctions::Abs'],
  [['sign'], 'FLOAT', ['DOUBLE'], 'impala::MathFunctions::Sign'],
  [['sin'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Sin'],
  [['asin'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Asin'],
  [['cos'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Cos'],
  [['acos'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Acos'],
  [['tan'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Tan'],
  [['atan'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Atan'],
  [['radians'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Radians'],
  [['degrees'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Degrees'],
  [['ceil', 'ceiling'], 'BIGINT', ['DOUBLE'], 'impala::MathFunctions::Ceil'],
  [['floor'], 'BIGINT', ['DOUBLE'], 'impala::MathFunctions::Floor'],
  [['round'], 'BIGINT', ['DOUBLE'], 'impala::MathFunctions::Round'],
  [['round'], 'DOUBLE', ['DOUBLE', 'INT'], 'impala::MathFunctions::RoundUpTo'],
  [['exp'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Exp'],
  [['ln'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Ln'],
  [['log10'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Log10'],
  [['log2'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Log2'],
  [['log'], 'DOUBLE', ['DOUBLE', 'DOUBLE'], 'impala::MathFunctions::Log'],
  [['pow', 'power'], 'DOUBLE', ['DOUBLE', 'DOUBLE'], 'impala::MathFunctions::Pow'],
  [['sqrt'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Sqrt'],
  [['rand'], 'DOUBLE', [], 'impala::MathFunctions::Rand',
   '_ZN6impala13MathFunctions11RandPrepareEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE'],
  [['rand'], 'DOUBLE', ['BIGINT'], 'impala::MathFunctions::RandSeed',
   '_ZN6impala13MathFunctions11RandPrepareEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE'],
  [['bin'], 'STRING', ['BIGINT'], 'impala::MathFunctions::Bin'],
  [['hex'], 'STRING', ['BIGINT'], 'impala::MathFunctions::HexInt'],
  [['hex'], 'STRING', ['STRING'], 'impala::MathFunctions::HexString'],
  [['unhex'], 'STRING', ['STRING'], 'impala::MathFunctions::Unhex'],
  [['conv'], 'STRING', ['BIGINT', 'TINYINT', 'TINYINT'],
   'impala::MathFunctions::ConvInt'],
  [['conv'], 'STRING', ['STRING', 'TINYINT', 'TINYINT'],
      'impala::MathFunctions::ConvString'],
  [['pmod'], 'BIGINT', ['BIGINT', 'BIGINT'], 'impala::MathFunctions::PmodBigInt'],
  [['pmod'], 'DOUBLE', ['DOUBLE', 'DOUBLE'], 'impala::MathFunctions::PmodDouble'],
  [['fmod'], 'FLOAT', ['FLOAT', 'FLOAT'], 'impala::MathFunctions::FmodFloat'],
  [['fmod'], 'DOUBLE', ['DOUBLE', 'DOUBLE'], 'impala::MathFunctions::FmodDouble'],
  [['positive'], 'TINYINT', ['TINYINT'],
   '_ZN6impala13MathFunctions8PositiveIN10impala_udf10TinyIntValEEET_PNS2_15FunctionContextERKS4_'],
  [['positive'], 'SMALLINT', ['SMALLINT'],
   '_ZN6impala13MathFunctions8PositiveIN10impala_udf11SmallIntValEEET_PNS2_15FunctionContextERKS4_'],
  [['positive'], 'INT', ['INT'],
   '_ZN6impala13MathFunctions8PositiveIN10impala_udf6IntValEEET_PNS2_15FunctionContextERKS4_'],
  [['positive'], 'BIGINT', ['BIGINT'],
   '_ZN6impala13MathFunctions8PositiveIN10impala_udf9BigIntValEEET_PNS2_15FunctionContextERKS4_'],
  [['positive'], 'FLOAT', ['FLOAT'],
   '_ZN6impala13MathFunctions8PositiveIN10impala_udf8FloatValEEET_PNS2_15FunctionContextERKS4_'],
  [['positive'], 'DOUBLE', ['DOUBLE'],
   '_ZN6impala13MathFunctions8PositiveIN10impala_udf9DoubleValEEET_PNS2_15FunctionContextERKS4_'],
  [['positive'], 'DECIMAL', ['DECIMAL'],
   '_ZN6impala13MathFunctions8PositiveIN10impala_udf10DecimalValEEET_PNS2_15FunctionContextERKS4_'],
  [['negative'], 'TINYINT', ['TINYINT'],
   '_ZN6impala13MathFunctions8NegativeIN10impala_udf10TinyIntValEEET_PNS2_15FunctionContextERKS4_'],
  [['negative'], 'SMALLINT', ['SMALLINT'],
   '_ZN6impala13MathFunctions8NegativeIN10impala_udf11SmallIntValEEET_PNS2_15FunctionContextERKS4_'],
  [['negative'], 'INT', ['INT'],
   '_ZN6impala13MathFunctions8NegativeIN10impala_udf6IntValEEET_PNS2_15FunctionContextERKS4_'],
  [['negative'], 'BIGINT', ['BIGINT'],
   '_ZN6impala13MathFunctions8NegativeIN10impala_udf9BigIntValEEET_PNS2_15FunctionContextERKS4_'],
  [['negative'], 'FLOAT', ['FLOAT'],
   '_ZN6impala13MathFunctions8NegativeIN10impala_udf8FloatValEEET_PNS2_15FunctionContextERKS4_'],
  [['negative'], 'DOUBLE', ['DOUBLE'],
   '_ZN6impala13MathFunctions8NegativeIN10impala_udf9DoubleValEEET_PNS2_15FunctionContextERKS4_'],
  [['negative'], 'DECIMAL', ['DECIMAL'],
   '_ZN6impala13MathFunctions8NegativeIN10impala_udf10DecimalValEEET_PNS2_15FunctionContextERKS4_'],
  [['quotient'], 'BIGINT', ['BIGINT', 'BIGINT'],
      'impala::MathFunctions::QuotientBigInt'],
  [['quotient'], 'BIGINT', ['DOUBLE', 'DOUBLE'],
      'impala::MathFunctions::QuotientDouble'],
  [['least'], 'TINYINT', ['TINYINT', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestIN10impala_udf10TinyIntValELb1EEET_PNS2_15FunctionContextEiPKS4_'],
  [['least'], 'SMALLINT', ['SMALLINT', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestIN10impala_udf11SmallIntValELb1EEET_PNS2_15FunctionContextEiPKS4_'],
  [['least'], 'INT', ['INT', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestIN10impala_udf6IntValELb1EEET_PNS2_15FunctionContextEiPKS4_'],
  [['least'], 'BIGINT', ['BIGINT', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestIN10impala_udf9BigIntValELb1EEET_PNS2_15FunctionContextEiPKS4_'],
  [['least'], 'FLOAT', ['FLOAT', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestIN10impala_udf8FloatValELb1EEET_PNS2_15FunctionContextEiPKS4_'],
  [['least'], 'DOUBLE', ['DOUBLE', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestIN10impala_udf9DoubleValELb1EEET_PNS2_15FunctionContextEiPKS4_'],
  [['least'], 'TIMESTAMP', ['TIMESTAMP', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestILb1EEEN10impala_udf12TimestampValEPNS2_15FunctionContextEiPKS3_'],
  [['least'], 'STRING', ['STRING', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestILb1EEEN10impala_udf9StringValEPNS2_15FunctionContextEiPKS3_'],
  [['least'], 'DECIMAL', ['DECIMAL', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestILb1EEEN10impala_udf10DecimalValEPNS2_15FunctionContextEiPKS3_'],
  [['greatest'], 'TINYINT', ['TINYINT', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestIN10impala_udf10TinyIntValELb0EEET_PNS2_15FunctionContextEiPKS4_'],
  [['greatest'], 'SMALLINT', ['SMALLINT', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestIN10impala_udf11SmallIntValELb0EEET_PNS2_15FunctionContextEiPKS4_'],
  [['greatest'], 'INT', ['INT', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestIN10impala_udf6IntValELb0EEET_PNS2_15FunctionContextEiPKS4_'],
  [['greatest'], 'BIGINT', ['BIGINT', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestIN10impala_udf9BigIntValELb0EEET_PNS2_15FunctionContextEiPKS4_'],
  [['greatest'], 'FLOAT', ['FLOAT', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestIN10impala_udf8FloatValELb0EEET_PNS2_15FunctionContextEiPKS4_'],
  [['greatest'], 'DOUBLE', ['DOUBLE', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestIN10impala_udf9DoubleValELb0EEET_PNS2_15FunctionContextEiPKS4_'],
  [['greatest'], 'TIMESTAMP', ['TIMESTAMP', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestILb0EEEN10impala_udf12TimestampValEPNS2_15FunctionContextEiPKS3_'],
  [['greatest'], 'STRING', ['STRING', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestILb0EEEN10impala_udf9StringValEPNS2_15FunctionContextEiPKS3_'],
  [['greatest'], 'DECIMAL', ['DECIMAL', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestILb0EEEN10impala_udf10DecimalValEPNS2_15FunctionContextEiPKS3_'],

  # Decimal Functions
  # TODO: oracle has decimal support for transcendental functions (e.g. sin()) to very
  # high precisions. Do we need them? It's unclear if other databases do the same.
  [['precision'], 'INT', ['DECIMAL'], 'impala::DecimalFunctions::Precision'],
  [['scale'], 'INT', ['DECIMAL'], 'impala::DecimalFunctions::Scale'],
  [['abs'], 'DECIMAL', ['DECIMAL'], 'impala::DecimalFunctions::Abs'],
  [['ceil', 'ceiling'], 'DECIMAL', ['DECIMAL'], 'impala::DecimalFunctions::Ceil'],
  [['floor'], 'DECIMAL', ['DECIMAL'], 'impala::DecimalFunctions::Floor'],
  [['round'], 'DECIMAL', ['DECIMAL'], 'impala::DecimalFunctions::Round'],
  [['round'], 'DECIMAL', ['DECIMAL', 'TINYINT'], 'impala::DecimalFunctions::RoundTo'],
  [['round'], 'DECIMAL', ['DECIMAL', 'SMALLINT'], 'impala::DecimalFunctions::RoundTo'],
  [['round'], 'DECIMAL', ['DECIMAL', 'INT'], 'impala::DecimalFunctions::RoundTo'],
  [['round'], 'DECIMAL', ['DECIMAL', 'BIGINT'], 'impala::DecimalFunctions::RoundTo'],
  [['truncate'], 'DECIMAL', ['DECIMAL'], 'impala::DecimalFunctions::Truncate'],
  [['truncate'], 'DECIMAL', ['DECIMAL', 'TINYINT'],
      'impala::DecimalFunctions::TruncateTo'],
  [['truncate'], 'DECIMAL', ['DECIMAL', 'SMALLINT'],
      'impala::DecimalFunctions::TruncateTo'],
  [['truncate'], 'DECIMAL', ['DECIMAL', 'INT'],
      'impala::DecimalFunctions::TruncateTo'],
  [['truncate'], 'DECIMAL', ['DECIMAL', 'BIGINT'],
      'impala::DecimalFunctions::TruncateTo'],

  # String builtin functions
  [['substr', 'substring'], 'STRING', ['STRING', 'BIGINT'],
   'impala::StringFunctions::Substring'],
  [['substr', 'substring'], 'STRING', ['STRING', 'BIGINT', 'BIGINT'],
   'impala::StringFunctions::Substring'],
  # left and right are key words, leave them out for now.
  [['strleft'], 'STRING', ['STRING', 'BIGINT'], 'impala::StringFunctions::Left'],
  [['strright'], 'STRING', ['STRING', 'BIGINT'], 'impala::StringFunctions::Right'],
  [['space'], 'STRING', ['BIGINT'], 'impala::StringFunctions::Space'],
  [['repeat'], 'STRING', ['STRING', 'BIGINT'], 'impala::StringFunctions::Repeat'],
  [['lpad'], 'STRING', ['STRING', 'BIGINT', 'STRING'], 'impala::StringFunctions::Lpad'],
  [['rpad'], 'STRING', ['STRING', 'BIGINT', 'STRING'], 'impala::StringFunctions::Rpad'],
  [['length'], 'INT', ['STRING'], 'impala::StringFunctions::Length'],
  [['length'], 'INT', ['CHAR'], 'impala::StringFunctions::CharLength'],
  [['char_length'], 'INT', ['STRING'], 'impala::StringFunctions::Length'],
  [['character_length'], 'INT', ['STRING'], 'impala::StringFunctions::Length'],
  [['lower', 'lcase'], 'STRING', ['STRING'], 'impala::StringFunctions::Lower'],
  [['upper', 'ucase'], 'STRING', ['STRING'], 'impala::StringFunctions::Upper'],
  [['initcap'], 'STRING', ['STRING'], 'impala::StringFunctions::InitCap'],
  [['reverse'], 'STRING', ['STRING'], 'impala::StringFunctions::Reverse'],
  [['translate'], 'STRING', ['STRING', 'STRING', 'STRING'],
   'impala::StringFunctions::Translate'],
  [['trim'], 'STRING', ['STRING'], 'impala::StringFunctions::Trim'],
  [['ltrim'], 'STRING', ['STRING'], 'impala::StringFunctions::Ltrim'],
  [['rtrim'], 'STRING', ['STRING'], 'impala::StringFunctions::Rtrim'],
  [['ascii'], 'INT', ['STRING'], 'impala::StringFunctions::Ascii'],
  [['instr'], 'INT', ['STRING', 'STRING'], 'impala::StringFunctions::Instr'],
  [['locate'], 'INT', ['STRING', 'STRING'], 'impala::StringFunctions::Locate'],
  [['locate'], 'INT', ['STRING', 'STRING', 'BIGINT'],
   'impala::StringFunctions::LocatePos'],
  [['regexp_extract'], 'STRING', ['STRING', 'STRING', 'BIGINT'],
   'impala::StringFunctions::RegexpExtract',
   '_ZN6impala15StringFunctions13RegexpPrepareEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE',
   '_ZN6impala15StringFunctions11RegexpCloseEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE'],
  [['regexp_replace'], 'STRING', ['STRING', 'STRING', 'STRING'],
   'impala::StringFunctions::RegexpReplace',
   '_ZN6impala15StringFunctions13RegexpPrepareEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE',
   '_ZN6impala15StringFunctions11RegexpCloseEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE'],
  [['concat'], 'STRING', ['STRING', '...'], 'impala::StringFunctions::Concat'],
  [['concat_ws'], 'STRING', ['STRING', 'STRING', '...'],
   'impala::StringFunctions::ConcatWs'],
  [['find_in_set'], 'INT', ['STRING', 'STRING'], 'impala::StringFunctions::FindInSet'],
  [['parse_url'], 'STRING', ['STRING', 'STRING'], 'impala::StringFunctions::ParseUrl',
   '_ZN6impala15StringFunctions15ParseUrlPrepareEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE',
   '_ZN6impala15StringFunctions13ParseUrlCloseEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE'],
  [['parse_url'], 'STRING', ['STRING', 'STRING', 'STRING'], 'impala::StringFunctions::ParseUrlKey',
   '_ZN6impala15StringFunctions15ParseUrlPrepareEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE',
   '_ZN6impala15StringFunctions13ParseUrlCloseEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE'],

  # Conditional Functions
  # Some of these have empty symbols because the BE special-cases them based on the
  # function name
  [['if'], 'BOOLEAN', ['BOOLEAN', 'BOOLEAN', 'BOOLEAN'], ''],
  [['if'], 'TINYINT', ['BOOLEAN', 'TINYINT', 'TINYINT'], ''],
  [['if'], 'SMALLINT', ['BOOLEAN', 'SMALLINT', 'SMALLINT'], ''],
  [['if'], 'INT', ['BOOLEAN', 'INT', 'INT'], ''],
  [['if'], 'BIGINT', ['BOOLEAN', 'BIGINT', 'BIGINT'], ''],
  [['if'], 'FLOAT', ['BOOLEAN', 'FLOAT', 'FLOAT'], ''],
  [['if'], 'DOUBLE', ['BOOLEAN', 'DOUBLE', 'DOUBLE'], ''],
  [['if'], 'STRING', ['BOOLEAN', 'STRING', 'STRING'], ''],
  [['if'], 'TIMESTAMP', ['BOOLEAN', 'TIMESTAMP', 'TIMESTAMP'], ''],
  [['if'], 'DECIMAL', ['BOOLEAN', 'DECIMAL', 'DECIMAL'], ''],

  [['nullif'], 'BOOLEAN', ['BOOLEAN', 'BOOLEAN'], ''],
  [['nullif'], 'TINYINT', ['TINYINT', 'TINYINT'], ''],
  [['nullif'], 'SMALLINT', ['SMALLINT', 'SMALLINT'], ''],
  [['nullif'], 'INT', ['INT', 'INT'], ''],
  [['nullif'], 'BIGINT', ['BIGINT', 'BIGINT'], ''],
  [['nullif'], 'FLOAT', ['FLOAT', 'FLOAT'], ''],
  [['nullif'], 'DOUBLE', ['DOUBLE', 'DOUBLE'], ''],
  [['nullif'], 'STRING', ['STRING', 'STRING'], ''],
  [['nullif'], 'TIMESTAMP', ['TIMESTAMP', 'TIMESTAMP'], ''],
  [['nullif'], 'DECIMAL', ['DECIMAL', 'DECIMAL'], ''],

  [['zeroifnull'], 'TINYINT', ['TINYINT'], 'impala::ConditionalFunctions::ZeroIfNull'],
  [['zeroifnull'], 'SMALLINT', ['SMALLINT'], 'impala::ConditionalFunctions::ZeroIfNull'],
  [['zeroifnull'], 'INT', ['INT'], 'impala::ConditionalFunctions::ZeroIfNull'],
  [['zeroifnull'], 'BIGINT', ['BIGINT'], 'impala::ConditionalFunctions::ZeroIfNull'],
  [['zeroifnull'], 'FLOAT', ['FLOAT'], 'impala::ConditionalFunctions::ZeroIfNull'],
  [['zeroifnull'], 'DOUBLE', ['DOUBLE'], 'impala::ConditionalFunctions::ZeroIfNull'],
  [['zeroifnull'], 'DECIMAL', ['DECIMAL'], 'impala::ConditionalFunctions::ZeroIfNull'],

  [['nullifzero'], 'TINYINT', ['TINYINT'], 'impala::ConditionalFunctions::NullIfZero'],
  [['nullifzero'], 'SMALLINT', ['SMALLINT'], 'impala::ConditionalFunctions::NullIfZero'],
  [['nullifzero'], 'INT', ['INT'], 'impala::ConditionalFunctions::NullIfZero'],
  [['nullifzero'], 'BIGINT', ['BIGINT'], 'impala::ConditionalFunctions::NullIfZero'],
  [['nullifzero'], 'FLOAT', ['FLOAT'], 'impala::ConditionalFunctions::NullIfZero'],
  [['nullifzero'], 'DOUBLE', ['DOUBLE'], 'impala::ConditionalFunctions::NullIfZero'],
  [['nullifzero'], 'DECIMAL', ['DECIMAL'], 'impala::ConditionalFunctions::NullIfZero'],

  [['isnull', 'ifnull', 'nvl'], 'BOOLEAN', ['BOOLEAN', 'BOOLEAN'], ''],
  [['isnull', 'ifnull', 'nvl'], 'TINYINT', ['TINYINT', 'TINYINT'], ''],
  [['isnull', 'ifnull', 'nvl'], 'SMALLINT', ['SMALLINT', 'SMALLINT'], ''],
  [['isnull', 'ifnull', 'nvl'], 'INT', ['INT', 'INT'], ''],
  [['isnull', 'ifnull', 'nvl'], 'BIGINT', ['BIGINT', 'BIGINT'], ''],
  [['isnull', 'ifnull', 'nvl'], 'FLOAT', ['FLOAT', 'FLOAT'], ''],
  [['isnull', 'ifnull', 'nvl'], 'DOUBLE', ['DOUBLE', 'DOUBLE'], ''],
  [['isnull', 'ifnull', 'nvl'], 'STRING', ['STRING', 'STRING'], ''],
  [['isnull', 'ifnull', 'nvl'], 'TIMESTAMP', ['TIMESTAMP', 'TIMESTAMP'], ''],
  [['isnull', 'ifnull', 'nvl'], 'DECIMAL', ['DECIMAL', 'DECIMAL'], ''],

  [['coalesce'], 'BOOLEAN', ['BOOLEAN', '...'], ''],
  [['coalesce'], 'TINYINT', ['TINYINT', '...'], ''],
  [['coalesce'], 'SMALLINT', ['SMALLINT', '...'], ''],
  [['coalesce'], 'INT', ['INT', '...'], ''],
  [['coalesce'], 'BIGINT', ['BIGINT', '...'], ''],
  [['coalesce'], 'FLOAT', ['FLOAT', '...'], ''],
  [['coalesce'], 'DOUBLE', ['DOUBLE', '...'], ''],
  [['coalesce'], 'STRING', ['STRING', '...'], ''],
  [['coalesce'], 'TIMESTAMP', ['TIMESTAMP', '...'], ''],
  [['coalesce'], 'DECIMAL', ['DECIMAL', '...'], ''],

  # Utility functions
  [['current_database'], 'STRING', [], 'impala::UtilityFunctions::CurrentDatabase'],
  [['user'], 'STRING', [], 'impala::UtilityFunctions::User'],
  [['sleep'], 'BOOLEAN', ['INT'], 'impala::UtilityFunctions::Sleep'],
  [['pid'], 'INT', [], 'impala::UtilityFunctions::Pid'],
  [['version'], 'STRING', [], 'impala::UtilityFunctions::Version'],
  [['typeOf'], 'STRING', ['BOOLEAN'], '_ZN6impala16UtilityFunctions6TypeOfIN10impala_udf10BooleanValEEENS2_9StringValEPNS2_15FunctionContextERKT_'],
  [['typeOf'], 'STRING', ['TINYINT'], '_ZN6impala16UtilityFunctions6TypeOfIN10impala_udf10TinyIntValEEENS2_9StringValEPNS2_15FunctionContextERKT_'],
  [['typeOf'], 'STRING', ['SMALLINT'], '_ZN6impala16UtilityFunctions6TypeOfIN10impala_udf11SmallIntValEEENS2_9StringValEPNS2_15FunctionContextERKT_'],
  [['typeOf'], 'STRING', ['INT'], '_ZN6impala16UtilityFunctions6TypeOfIN10impala_udf6IntValEEENS2_9StringValEPNS2_15FunctionContextERKT_'],
  [['typeOf'], 'STRING', ['BIGINT'], '_ZN6impala16UtilityFunctions6TypeOfIN10impala_udf9BigIntValEEENS2_9StringValEPNS2_15FunctionContextERKT_'],
  [['typeOf'], 'STRING', ['FLOAT'], '_ZN6impala16UtilityFunctions6TypeOfIN10impala_udf8FloatValEEENS2_9StringValEPNS2_15FunctionContextERKT_'],
  [['typeOf'], 'STRING', ['DOUBLE'], '_ZN6impala16UtilityFunctions6TypeOfIN10impala_udf9DoubleValEEENS2_9StringValEPNS2_15FunctionContextERKT_'],
  [['typeOf'], 'STRING', ['CHAR'], '_ZN6impala16UtilityFunctions6TypeOfIN10impala_udf9StringValEEES3_PNS2_15FunctionContextERKT_'],
  [['typeOf'], 'STRING', ['VARCHAR'], '_ZN6impala16UtilityFunctions6TypeOfIN10impala_udf9StringValEEES3_PNS2_15FunctionContextERKT_'],
  [['typeOf'], 'STRING', ['STRING'], '_ZN6impala16UtilityFunctions6TypeOfIN10impala_udf9StringValEEES3_PNS2_15FunctionContextERKT_'],
  [['typeOf'], 'STRING', ['TIMESTAMP'], '_ZN6impala16UtilityFunctions6TypeOfIN10impala_udf12TimestampValEEENS2_9StringValEPNS2_15FunctionContextERKT_'],
  [['typeOf'], 'STRING', ['DECIMAL'], '_ZN6impala16UtilityFunctions6TypeOfIN10impala_udf10DecimalValEEENS2_9StringValEPNS2_15FunctionContextERKT_'],
  [['fnv_hash'], 'BIGINT', ['TINYINT'],
   '_ZN6impala16UtilityFunctions7FnvHashIN10impala_udf10TinyIntValEEENS2_9BigIntValEPNS2_15FunctionContextERKT_'],
  [['fnv_hash'], 'BIGINT', ['SMALLINT'],
   '_ZN6impala16UtilityFunctions7FnvHashIN10impala_udf11SmallIntValEEENS2_9BigIntValEPNS2_15FunctionContextERKT_'],
  [['fnv_hash'], 'BIGINT', ['INT'],
   '_ZN6impala16UtilityFunctions7FnvHashIN10impala_udf6IntValEEENS2_9BigIntValEPNS2_15FunctionContextERKT_'],
  [['fnv_hash'], 'BIGINT', ['BIGINT'],
   '_ZN6impala16UtilityFunctions7FnvHashIN10impala_udf9BigIntValEEES3_PNS2_15FunctionContextERKT_'],
  [['fnv_hash'], 'BIGINT', ['FLOAT'],
   '_ZN6impala16UtilityFunctions7FnvHashIN10impala_udf8FloatValEEENS2_9BigIntValEPNS2_15FunctionContextERKT_'],
  [['fnv_hash'], 'BIGINT', ['DOUBLE'],
   '_ZN6impala16UtilityFunctions7FnvHashIN10impala_udf9DoubleValEEENS2_9BigIntValEPNS2_15FunctionContextERKT_'],
  [['fnv_hash'], 'BIGINT', ['STRING'],
   '_ZN6impala16UtilityFunctions13FnvHashStringEPN10impala_udf15FunctionContextERKNS1_9StringValE'],
  [['fnv_hash'], 'BIGINT', ['TIMESTAMP'],
   '_ZN6impala16UtilityFunctions16FnvHashTimestampEPN10impala_udf15FunctionContextERKNS1_12TimestampValE'],
  [['fnv_hash'], 'BIGINT', ['DECIMAL'],
   '_ZN6impala16UtilityFunctions14FnvHashDecimalEPN10impala_udf15FunctionContextERKNS1_10DecimalValE'],
]
