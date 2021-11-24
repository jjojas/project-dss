import React from 'react';
import TagInput from './commons/tagInput';
import Button from '@mui/material/Button';


class Main  extends React.Component {
    state = {
        judulNovel : [],
        genreNovel : []
    }


    render() { 
        return (
        <div>
            <h1 >Sistem Rekomendasi Novel</h1>
            <form>
                <h3 >Masukkan judul novel yang pernah dibaca :</h3>
                <TagInput tags={[]} placeholder={"ketikkan judul novel"} />
                <h3 >Masukkan genre novel yang diingingkan :</h3>
                <TagInput tags={[]} placeholder={"Ketikkan genre novel"} />
                <Button variant="contained" id="tombol" color="secondary">Cari rekomendasi</Button>
            </form>
        </div>
        );
    }
}
 
export default Main;