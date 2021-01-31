import AppBar from '@material-ui/core/AppBar';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import Backdrop from '@material-ui/core/Backdrop';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <AppBar style={{backgroundColor: "#232323"}}>
          <Typography>
          <h1 align="center">Howdy!</h1>
          </Typography>
        </AppBar>

        
        
        <Grid align="center">Test1</Grid>
      </header>
    </div>
  );
}

export default App;
