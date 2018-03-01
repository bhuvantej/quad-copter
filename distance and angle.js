# quad-copter
#codes for distance n angle.
latp1=17.393591;
longp1=78.319936;
latp2=17.400657;
longp2=78.331709;

function toRadians(x){
	return x*(22/7)/180;
}
function toDegrees(x){
	return x*180/(22/7);
}
var R = 6371e3; // metres
var φ1 = toRadians(lat1);
var φ2 = toRadians(lat2);
var Δφ = toRadians((lat2-lat1));
var Δλ = toRadians((lon2-lon1));

var a = Math.sin(Δφ/2) * Math.sin(Δφ/2) +
        Math.cos(φ1) * Math.cos(φ2) *
        Math.sin(Δλ/2) * Math.sin(Δλ/2);
var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));

var d = R * c;

console.log(d);
λ1=longp1;
λ2=longp2;
φ1=latp1;
φ2=latp2;
var y = Math.sin(λ2-λ1) * Math.cos(φ2);
var x = Math.cos(φ1)*Math.sin(φ2) -
        Math.sin(φ1)*Math.cos(φ2)*Math.cos(λ2-λ1);
var brng = toDegrees(Math.atan2(y, x));

console.log(brng);
