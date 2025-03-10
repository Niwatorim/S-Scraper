//for scalability

//dependencies
import express from 'express';
import {question} from '../controller/alg.controller.js'

const router = express.Router();

router.post('/', question);
export default router;