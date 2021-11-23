import React from 'react';
import { Route, Redirect, Switch } from 'react-router-dom';
import Main from './components/main';



const App = () => {
  return ( 
    <React.Fragment>
      <Switch>
        <Route path="/main" component={Main}></Route>
        <Route path="/table" component={}></Route>
        <Redirect from="/" exact to="/main" />
      </Switch>
    </React.Fragment> 
   );
}
 
export default App;
