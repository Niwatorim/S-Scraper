import {Container, IconButton, Input, Typography } from '@mui/material'
import {} from 'react'

function HomePage() {
  return (
    <Container>
        {/* Main Header */}
        <Typography fontSize={'30'} fontWeight={'bold'} variant='h1'
        sx={{
            fontSize:{ xs:28, md:22},
            backgroundColor: 'primary',
            textAlign:'center',
        }}>
            Home Page
        </Typography>
        
        
        <Input> {/* Main Input */}

        </Input>
        <IconButton> {/* Submission button */}
            {/* use React Icon here */}
        </IconButton>



    </Container>
  )
}

export default HomePage