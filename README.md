# Genetic Programming Firs Try
Having no knowledge of the way genetic programs are written, I am setting out to write one which calculates the regression of a set of points
#What I know
I understand the basic concepts of genetic programming--you kill the least fit in a population then, to create more diversity, mutate the population. Other than that, I have never read a genetic program or a genetic programming guide.
#How it works
<ol>
  <li>Takes in a set of points</li>
  <li>Generates 64 random equations from the original '1'<br />then loops</li>
  <ol>
    <li>calculates the fitness of each equation by:<ol>
      <li>...running it with the x value as each of the inputs' x values, then</li>
      <li>...takes the difference between the output value and the chosen input's y value</li>
    </ol></li>
    <li>Then kills the least fit half</li>
    <li>Then mutates each of the population in duplicate, doubling the population</li>
  </ol>
</ol>
