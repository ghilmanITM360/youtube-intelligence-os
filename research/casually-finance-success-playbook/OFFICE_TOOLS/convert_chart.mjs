import sharp from 'sharp';
await sharp(process.argv[2],{density:180}).png().toFile('/private/tmp/cf-performance-chart.png');
