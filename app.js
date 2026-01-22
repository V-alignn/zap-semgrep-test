const express = require('express');
const app = express();

const PORT = 3030;

app.get('/login', (req, res) => {
  const user = req.query.user || '';
  res.send("Hello " + user);
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`App running on port ${PORT}`);
});
