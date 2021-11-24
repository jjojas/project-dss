import React from 'react';
import { Route, Redirect, Switch } from 'react-router-dom';
import Main from './components/main';



class App extends React.Component {

  render() {
  return ( 
    <React.Fragment>
      <main>
        <Switch>
          <Route path="/main" component={Main}></Route>
          <Redirect from="/" exact to="/main" />
          <Redirect to="/not-found" />
        </Switch>
      </main>
    </React.Fragment> 
   );
  }
}
 
export default App;
