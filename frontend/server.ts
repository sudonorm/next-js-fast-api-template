import express, { Request, Response } from 'express';
import https from 'https';
import fs from 'fs';
import path from 'path';
import next from 'next';

const dev = process.env.NODE_ENV !== 'production';
const app = next({ dev });
const handle = app.getRequestHandler();

const httpsOptions = {
  key: fs.readFileSync(path.join(__dirname, 'localhost-key.pem')),
  cert: fs.readFileSync(path.join(__dirname, 'localhost.pem')),
};

app.prepare().then(() => {
  const server = express();

  // Middleware to parse JSON
  server.use(express.json());

  // Handle all other routes with Next.js
  server.all('*', (req: Request, res: Response) => {
    return handle(req, res);
  });

  // https.createServer(httpsOptions, server).listen(3000, (err?: Error) => {
  https.createServer(httpsOptions, server).listen(3000, (err?: Error) => {
    if (err) throw err;
    console.log('> Ready on https://localhost:3000');
  });
});
