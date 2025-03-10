//setup
import express from 'express'
import dotenv from 'dotenv'
import productRoutes from './routes/alg.routes.js';
dotenv.config();

const app = express();
app.use(express.json()); //allows for json data
const PORT = process.env.PORT;

app.use('/api/alg', alg.routes.js);

app.listen(PORT,()=>{
    connect();
    console.log(`server started at http://localhost:${PORT}`);
});