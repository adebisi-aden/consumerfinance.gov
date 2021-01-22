/* eslint complexity: ["error", 8] */
/* eslint max-params: ["error", 8] */
// Polyfill Promise for IE11
import 'core-js/features/promise';

import Highcharts from 'highcharts/highstock';
import accessibility from 'highcharts/modules/accessibility';
import chartHooks from './chart-hooks.js';
import defaultBar from './bar-styles.js';
import defaultDatetime from './datetime-styles.js';
import defaultLine from './line-styles.js';
import fetch from 'cross-fetch';

accessibility( Highcharts );

/**
 * Fetches JSON data
 * @param {string} url The url to fetch data from
 * @returns {Promise} Promise that resolves to JSON data
 */
function fetchData( url ) {
  return fetch( url ).then( res => res.json() );
}

/**
 * Selects appropriate chart import style
 * @param {string} type The chart type as defined in the organism
 * @returns {object} The appropriately loaded style object
 */
function getDefaultChartObject( type ) {
  switch ( type ) {
    case 'bar':
      return defaultBar;
    case 'datetime':
      return defaultDatetime;
    case 'line':
      return defaultLine;
    default:
      throw new Error( 'Unknown chart type specified' );
  }
}

/**
 * Overrides default chart options using provided Wagtail configurations
 * @param {object} data The data to provide to the chart
 * @param {object} dataProps (destructured) data-* props attached to the chart HTML
 * @returns {object} The configured style object
 */
function makeChartOptions(
  data,
  { chartType, styleOverrides, description, xAxisLabel, yAxisLabel }
) {
  const defaultObj = JSON.parse(
    JSON.stringify( getDefaultChartObject( chartType ) )
  );

  if ( styleOverrides ) {
    const styles = JSON.parse( styleOverrides );
    Object.keys( styles ).forEach( key => {
      const override = resolveOverride( styles[key], data );
      key.split( '.' ).reduce( ( acc, curr, i, arr ) => {
        if ( i === arr.length - 1 ) return ( acc[curr] = override );
        if ( !acc[curr] ) acc[curr] = {};
        return acc[curr];
      }, defaultObj );
    } );
  }

  /* eslint-disable-next-line */
  defaultObj.title = { text: undefined };
  defaultObj.series = [ { data } ];
  defaultObj.accessibility.description = description;
  defaultObj.yAxis.title.text = yAxisLabel;
  if ( xAxisLabel ) defaultObj.xAxis.title.text = xAxisLabel;

  return defaultObj;
}

/**
 * Mechanism for passing functions or applied functions to the chart style object
 * @param {string} override Prefixed refered to a function in chart-hooks.js
 * @param {string} data Data provided to chart
 * @returns {function|string} Result of the override or the provided unmatched style
 */
function resolveOverride( override, data ) {
  if ( typeof override === 'string' ) {
    if ( override.match( /^fn__/ ) ) {
      return chartHooks[override.replace( 'fn__', '' )];
    } else if ( override.match( /^hook__/ ) ) {
      return chartHooks[override.replace( 'hook__', '' )]( data );
    }
  }
  return override;
}

/**
 * Selects whether to use inline data or fetch data that matches a url
 * @param {string} source Source provided from wagtail
 * @returns {Promise} Promise resolving to either fetched JSON or parsed inline JSON
 */
function resolveData( source ) {
  if ( source.match( /^http/i ) ) {
    return fetchData( source );
  }
  return Promise.resolve( JSON.parse( source ) );
}

/**
 * Wires up select filters, if present
 * @param {object} filter Object with a filter key and possible label
 * @param {object} data The raw chart data, untransformed
 * @returns {array} List of options for the select
 */
function getOptions( filter, data ) {
  const vals = {};
  const { key } = filter;
  data.forEach( d => {
    let item = d[key];
    if ( !Array.isArray( item ) ) item = [ item ];
    item.forEach( v => {
      vals[v] = 1;
    } );
  } );

  return Object.keys( vals );
}

/**
 * @param {array} options List of options to build for the select component
 * @param {object} chartNode The DOM node of the current chart
 * @param {object} filter key and possible label to filter on
 * @returns {object} the built select DOM node
 */
function makeFilterDOM( options, chartNode, filter ) {
  const name = filter.label ? filter.label : filter.key;
  const id = Math.random() + name;
  const attachPoint = chartNode.getElementsByClassName( 'chart-selects' )[0];

  const wrapper = document.createElement( 'div' );
  wrapper.className = 'select-wrapper m-form-field m-form-field__select';

  const label = document.createElement( 'label' );
  label.className = 'a-label a-label__heading';
  label.innerText = 'Select ' + name;
  label.htmlFor = id;

  const selectDiv = document.createElement( 'div' );
  selectDiv.className = 'a-select';

  const select = document.createElement( 'select' );
  select.id = id;
  select.dataset.key = filter.key;

  const allOpt = document.createElement( 'option' );
  allOpt.value = '';
  allOpt.innerText = 'View All';
  select.appendChild( allOpt );

  options.forEach( option => {
    const opt = document.createElement( 'option' );
    opt.value = option;
    opt.innerText = option;
    select.appendChild( opt );
  } );

  selectDiv.appendChild( select );
  wrapper.appendChild( label );
  wrapper.appendChild( selectDiv );
  attachPoint.appendChild( wrapper );

  return select;
}

/**
 * @param {object} chartNode The DOM node of the current chart
 * @returns {object} the built select DOM node
 */
function makeSelectHeaderDOM( chartNode ) {
  const attachPoint = chartNode.getElementsByClassName( 'chart-selects' )[0];
  const selectHeader = document.createElement( 'h3' );
  selectHeader.innerText = 'Total ' + attachPoint.dataset.title;
  attachPoint.appendChild( selectHeader );

  return selectHeader;
}

/**
 * @param {object} selectNode The DOM node of the select component
 * @param {object} chartNode The DOM node of the chart
 * @param {object} chart The Highcharts chart object
 * @param {object} filter The filter key and possible label
 * @param {object} data The raw chart data, untransformed
 * @param {function} transform The transform function for this chart
 */
function attachFilter(
  selectNode, chartNode, chart, filter, data, transform
) {
  const attachPoint = chartNode.getElementsByClassName( 'chart-selects' )[0];
  const selectHeader = attachPoint.querySelector( 'h3' );
  const { title } = attachPoint.dataset;
  selectNode.addEventListener( 'change', () => {
    // filter on all selects
    const selects = chartNode.querySelectorAll( '.a-select > select' );
    let filtered = data;
    let headerText = 'Total ' + title;
    let isFirst = true;

    for ( let i = 0; i < selects.length; i++ ) {
      const curr = selects[i];
      const { value } = curr;
      if ( value ) {
        if ( isFirst ) {
          headerText = title + ' for ' + value;
          isFirst = false;
        } else {
          headerText = headerText + ' and ' + value;
        }
      }

      filtered = chartHooks.filter(
        filtered, curr.dataset.key, value );
    }

    if ( transform ) {
      filtered = transform( filtered );
    }

    selectHeader.innerText = headerText;
    chart.series[0].setData( filtered );

  } );
}

/** Wires up select filters, if present
  * @param {string} filters Stringified JSON array of objects
  * @param {object} chartNode The DOM node of the current chart
  * @param {object} chart The initialized chart
  * @param {object} data The raw chart data, untransformed
  * @param {function} transform The transform function for this chart
  * */
function initFilters( filters, chartNode, chart, data, transform ) {
  if ( !filters ) return;
  try {
    filters = JSON.parse( filters );
    const selects = [];
    if ( !Array.isArray( filters ) ) filters = [ filters ];
    filters.forEach( filter => {
      const options = getOptions( filter, data );
      selects.push( makeFilterDOM( options, chartNode, filter ) );
    } );
    if ( selects.length ) {
      makeSelectHeaderDOM( chartNode );
      selects.forEach( ( selectNode, i ) => {
        attachFilter(
          selectNode, chartNode, chart, filters[i], data, transform
        );
      } );
    }
  } catch ( err ) {
    console.error( err );
    console.error( 'Bad JSON in chart filters ', filters );
  }
}

/**
 * Initializes every chart on the page
 */
function buildCharts() {
  const charts = document.getElementsByClassName( 'o-simple-chart' );
  for ( let i = 0; i < charts.length; i++ ) {
    buildChart( charts[i] );
  }
}

/**
 * Initializes a chart
 * @param {object} chartNode The DOM node of the current chart
 */
function buildChart( chartNode ) {
  const target = chartNode.getElementsByClassName( 'simple-chart-target' )[0];
  const { source, transform, filters } = target.dataset;

  resolveData( source.trim() ).then( d => {
    const data =
      transform && chartHooks[transform] ? chartHooks[transform]( d ) : d;
    const chart = Highcharts.chart(
      target,
      makeChartOptions( data, target.dataset )
    );
    initFilters(
      filters, chartNode, chart, d, transform && chartHooks[transform]
    );
  } );
}

buildCharts();
