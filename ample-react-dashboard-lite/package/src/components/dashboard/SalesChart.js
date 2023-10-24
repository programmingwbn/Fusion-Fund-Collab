import { Card, CardBody, CardSubtitle, CardTitle } from "reactstrap";
import Chart from "react-apexcharts";

const SalesChart = () => {
  const chartoptions = {
    series: [
      {
        name: "OpenAI",
        data: [0, 31, 40, 28, 51, 42, 109, 100],
      },
      {
        name: "Facebook",
        data: [0, 11, 32, 45, 32, 34, 52, 41],
      },
      {
        name: "Company #3",
        data: [0, 4, 21, 30, 38, 41, 44, 55],
      },
      {
        name: "Company #4",
        data: [0, 17, 21, 26, 47, 59, 76, 84],
      },
      {
        name: "Company #5",
        data: [0, 7, 11, 15, 39, 51, 67, 80],
      }
    ],
    options: {
      chart: {
        type: "area",
      },
      dataLabels: {
        enabled: false,
      },
      grid: {
        strokeDashArray: 3,
      },

      stroke: {
        curve: "smooth",
        width: 1,
      },
      xaxis: {
        categories: [
          "Jan",
          "Feb",
          "March",
          "April",
          "May",
          "June",
          "July",
          "Aug",
        ],
      },
    },
  };
  return (
    <Card>
      <CardBody>
        <CardTitle tag="h5">Companies summary</CardTitle>
        <CardSubtitle className="text-muted" tag="h6">
          Frequency of hits using keywords
        </CardSubtitle>
        <Chart
          type="area"
          width="100%"
          height="390"
          options={chartoptions.options}
          series={chartoptions.series}
        ></Chart>
      </CardBody>
    </Card>
  );
};

export default SalesChart;
