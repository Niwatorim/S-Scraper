
import {Box} from '@mui/material'
import {Routes, Route} from 'react-router-dom'
import HomePage from './pages/HomePage'
import Answer from './pages/Answer'

function App() {
  
  return (
    <Box minHeight={'100vh'}>
      <Routes>
        <Route path='/' element={<HomePage/>} />
        <Route path='/answer' element={<Answer/>}/>
      </Routes>
    </Box>
  
  )
}

export default App
