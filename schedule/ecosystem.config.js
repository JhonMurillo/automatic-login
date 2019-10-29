module.exports = {
  apps: [
    {
      name: 'schedule-automatic-login',
      script: 'index.js',
      instances: 1,
      exec_mode: 'fork',
      max_memory_restart: '250M',
      log_date_format: 'YYYY/MM/DD HH:mm:ss',
      env: {
        NODE_ENV: 'production',
        FREQUENCY: '*/1 * * * *'
      }
    }
  ]
};
