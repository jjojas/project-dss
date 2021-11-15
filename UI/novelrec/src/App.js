import React from 'react'
import TagInput from './components/tagInput';
import animasi from './animasibuku.jpg';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';




const App = () => {
  return ( 
    <React.Fragment>
      <Grid>
        <h1 >Sistem Rekomendasi Novel</h1>
        <h3 >Masukkan judul novel yang pernah dibaca :</h3>
        <TagInput tags={[]} placeholder={"ketikkan judul novel"} />
        <h3 >Masukkan genre novel yang diingingkan :</h3>
        <TagInput tags={[]} placeholder={"Ketikkan genre novel"} />
        <Button variant="contained" id="tombol" color="secondary">Cari rekomendasi</Button>
      </Grid>
    </React.Fragment> 
   );
}
 
export default App;
