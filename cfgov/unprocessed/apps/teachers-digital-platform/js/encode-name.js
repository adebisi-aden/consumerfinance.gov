/**
 * Simple ROT13-style rotational cipher
 *
 * @param {string} str Input
 * @returns {string} Rotated string
 */
function rotate( str ) {
  const list1 = './-:?=&%# ZQXJKVWPY abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHILMNORSTU';
  const list2 = 'ZQXJKVWPY ./-:?=&%# 123456789ABCDEFGHILMNORSTUabcdefghijklmnopqrstuvwxyz';

  return str
    .split( '' )
    .map( char => {
      const idx = list1.indexOf( char );
      return idx === -1 ? char : list2[idx];
    } )
    .join( '' );
}

/**
 * Create a hash code for a string (legacy encoding)
 *
 * Adapted from https://stackoverflow.com/a/7616484/3779
 *
 * @param {string} str String to hash
 * @returns {string} Hash code
 */
function hashCode( str ) {
  let hash = 0;
  for ( let i = 0; i < str.length; i++ ) {
    const chr = str.charCodeAt( i );
    hash = ( ( hash << 5 ) - hash ) + chr;
    // Convert to 32bit integer
    hash |= 0;
  }

  return Number( hash ).toString( 36 );
}

/**
 * XOR a string (legacy encoding)
 *
 * Based on XOR Crypt v1.1.1 - http://github.com/RobLoach/xor-crypt
 * @license MIT
 *   http://opensource.org/licenses/MIT
 *
 * @param {string} str Input
 * @param {number} key Number to apply
 * @returns {string} Output
 */
function xor( str, key ) {
  return str.split( '' )
    .map( letter => String.fromCharCode( key ^ letter.charCodeAt( 0 ) ) )
    .join( '' );
}

// Some simple obfuscation when minified
const wwindow = window;
const xtoy = 'xtoy';
const a = 'a';
const b = 'b';
const x = 'x';
const y = 'y';
const btoa = xtoy.replace( x, b ).replace( y, a );
const atob = xtoy.replace( x, a ).replace( y, b );
const base64Encode = wwindow[btoa];
const base64Decode = wwindow[atob];
const base64UrlEncode = val => base64Encode( val )
  .replace( /\+/g, '-' )
  .replace( /\//g, '_' );
const base64UrlDecode = val => base64Decode(
  val
    .replace( /-/g, '+' )
    .replace( /_/g, '/' )
);

/**
 * Encode string
 *
 * @param {string} input Input
 * @returns {string} Encoded string
 */
function encode( input ) {
  return '==' + base64UrlEncode( rotate(
    `${ input }${ input }${ input }`
  ) );
}

/**
 * Decode a string
 *
 * @param {string} encoded Encoded string
 * @returns {string | null} Decoded string (or null)
 */
function decode( encoded ) {
  if ( encoded.indexOf( '==' ) !== 0 ) {
    return legacyDecode( encoded );
  }

  // New version uses leading "==" and Base64 for URLs
  let b64Decoded;
  try {
    b64Decoded = base64UrlDecode( encoded.substr( 2 ) );
  } catch ( err ) {
    return null;
  }

  const three = rotate( b64Decoded );
  const out = three.substr( 0, three.length / 3 );
  if ( three !== `${ out }${ out }${ out }` ) {
    // Tampered
    return null;
  }

  return out;
}

/**
 * Decode a string with legacy strategy
 *
 * @param {string} encoded Encoded string
 * @returns {string | null} Decoded string (or null)
 */
function legacyDecode( encoded ) {
  let b64Decoded;

  try {
    b64Decoded = base64Decode( encoded );
  } catch ( err ) {
    return null;
  }

  const m = b64Decoded.match( /^(\w+)\.(\w+)\.(.*)/ );
  if ( !m ) {
    // Looks wrong
    return null;
  }

  const [ , keyB36, hashExpected, xored ] = m;
  const key = parseInt( keyB36, 36 );
  const plain = xor( xored, key );

  return hashCode( plain ) === hashExpected ? plain : null;
}

/**
 * Encode name as a URL hash
 *
 * @param {string} url URL
 * @param {string} name Name
 * @returns {string} Output URL
 */
function encodeNameInUrl( url, name ) {
  return url.replace( /#.*/, '' ) + '#' + encode( name );
}

/**
 * Decode name from a URL
 *
 * @param {string} url URL
 * @returns {string | null} Name, if set and valid
 */
function decodeNameFromUrl( url ) {
  return decode( url.replace( /^[^#]*#/, '' ) );
}

export {
  encodeNameInUrl,
  decodeNameFromUrl
};
