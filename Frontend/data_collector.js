const https = require('https');
const fs = require('fs');
async function getData(){
    const keyW = "19D0E5BD-C8D9-11ED-B6F4-42010A800007";
    const keyR = "ADE813DD-C8D2-11ED-B6F4-42010A800007";
    const fields = "name,model,hardware,location_type,position_rating,led_brightness,firmware_version,rssi,uptime,pa_latency,memory,last_seen,last_modified,date_created,channel_state,channel_flags,channel_flags_manual,channel_flags_auto,confidence,humidity,temperature,pressure,analog_input,pm1.0,pm1.0_atm,pm1.0_cf_1,pm2.5_alt,pm2.5,pm2.5_atm,pm2.5_cf_1,pm2.5_10minute,pm2.5_30minute,pm2.5_60minute,pm2.5_6hour,pm2.5_24hour,pm2.5_1week,pm10.0,pm10.0_atm,pm10.0_cf_1,scattering_coefficient,deciviews,visual_range,0.3_um_count,0.5_um_count,1.0_um_count,2.5_um_count,5.0_um_count,10.0_um_count";    
    const url = "https://api.purpleair.com/v1/groups/1684/members?api_key="+keyR+"&fields="+fields;
    
    return new Promise((resolve) => {
        https.get(url,(resp) => {
            let data = '';
            resp.on('data',(chunk) => {
                data+=chunk;
            });
            resp.on('end', () => {
                resolve(doWhatever(JSON.parse(data)));
            });
        });
    })
}
getData();

function doWhatever(jsondata){
    for(i=0;i<jsondata.fields.length;i++){
        fs.appendFileSync('../Data/Raw/data.csv',jsondata.fields[i], err => {
            if (err) {
              console.error(err);
            }
          });
        if(i<jsondata.fields.length-1)
        fs.appendFileSync('../Data/Raw/data.csv',",", err => {
            if (err) {
              console.error(err);
            }
          });
    }
    for(i=0;i<jsondata.data.length;i++){
        fs.appendFileSync('../Data/Raw/data.csv','\n', err => {
            if (err) {
              console.error(err);
            }
          });
        for(j=0;j<jsondata.data[i].length;j++){
            fs.appendFileSync('../Data/Raw/data.csv',jsondata.data[i][j], err => {
                if (err) {
                  console.error(err);
                }
              });
            if(j<jsondata.data[i].length-1)
            fs.appendFileSync('../Data/Raw/data.csv',",", err => {
                if (err) {
                  console.error(err);
                }
              });
        }
        
    }
}

