const scheduler = require('node-schedule');
const nrc = require('node-run-cmd');

const cronJob = scheduler.scheduleJob('*/1 * * * *', () => {
  try {
    nrc.run('python3 ../InstaBot.py');
  } catch (error) {
    console.error(error);
  }
});
