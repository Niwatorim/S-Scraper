import { useEffect } from 'react'
import {Container} from '@mui/material'
import { cardDataStore } from '../store/CardStore'



function Answer() {
  const {requestData, cardData} = cardDataStore();
  useEffect(()=>
  {
    requestData();
  },[requestData]) 


  return (
    <Container>


    </Container>
  )
}

export default Answer