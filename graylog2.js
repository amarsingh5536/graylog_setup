// graylog2 node js module for logger data to graylog
const graylog2 = require('graylog2');
const logger = new graylog2.graylog({
    servers: [{ host: '192.168.205.18', port: 12201 }] // Replace the "host" per your Graylog domain
  });

logger.log('Hello Graylog campaign.')