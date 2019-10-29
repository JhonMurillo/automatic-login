const scheduler = require('node-schedule');
const nrc = require('node-run-cmd');
const { FREQUENCY } = process.env;

const cronJob = scheduler.scheduleJob(FREQUENCY, () => {
  try {
    nrc.run('python3 ../InstaBot.py path');
    console.info('executed ;-)');
  } catch (error) {
    console.error(error);
  }
});
