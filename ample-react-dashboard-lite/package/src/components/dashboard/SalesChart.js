import { Card, CardBody, CardSubtitle, CardTitle } from "reactstrap";
import Chart from "react-apexcharts";
import React from "react";
// import record from "./test.json";

const SalesChart = () => {
  const [chartoptions, setChartData] = React.useState(null);
  async function fetchDataFromDummyAPI() {
    try {
      const response = await fetch('https://jsonplaceholder.typicode.com/posts/1'); // Replace with your dummy API URL
      // if (!response.ok) {
      //   throw new Error('Failed to fetch data from the API');
      // }
  
      // const data = await response.json();
      const data={
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
      return data;
    } catch (error) {
      console.error('Error:', error);
      return null;
    }
  }
  React.useEffect(() => {
    async function fetchData() {
      try {
        const data = await fetchDataFromDummyAPI();
        if (data) {
          setChartData(data);
        } else {
          console.log('Failed to fetch data from the API.');
        }
      } catch (error) {
        console.error('An error occurred:', error);
      }
    }

    fetchData();
  }, []);
  // try {
  //  const chartData = await fetchDataFromDummyAPI();
  // }

  //    catch (error) {
  //     console.error('An error occurred:', error);
  //   }


  // async function getChartData() {
  //   try {
  //     const apiData = await fetchDataFromDummyAPI();
  //     if (apiData) {
  //       console.log('Data from the API:', apiData);
  //       // You can work with the data here.
  //     } else {
  //       console.log('Failed to fetch data from the API.');
  //     }
  //   } catch (error) {
  //     console.error('An error occurred:', error);
  //   }
  // }
  // const chartoptions = {
  //   series: [
  //     {
  //       name: "OpenAI",
  //       data: [0, 31, 40, 28, 51, 42, 109, 100],
  //     },
  //     {
  //       name: "Facebook",
  //       data: [0, 11, 32, 45, 32, 34, 52, 41],
  //     },
  //     {
  //       name: "Company #3",
  //       data: [0, 4, 21, 30, 38, 41, 44, 55],
  //     },
  //     {
  //       name: "Company #4",
  //       data: [0, 17, 21, 26, 47, 59, 76, 84],
  //     },
  //     {
  //       name: "Company #5",
  //       data: [0, 7, 11, 15, 39, 51, 67, 80],
  //     }
  //   ],
  //   options: {
  //     chart: {
  //       type: "area",
  //     },
  //     dataLabels: {
  //       enabled: false,
  //     },
  //     grid: {
  //       strokeDashArray: 3,
  //     },

  //     stroke: {
  //       curve: "smooth",
  //       width: 1,
  //     },
  //     xaxis: {
  //       categories: [
  //         "Jan",
  //         "Feb",
  //         "March",
  //         "April",
  //         "May",
  //         "June",
  //         "July",
  //         "Aug",
  //       ],
  //     },
  //   },
  // };
  return (
    <Card>
      <CardBody>
        <CardTitle tag="h5">Companies summary</CardTitle>
        <CardSubtitle className="text-muted" tag="h6">
          Frequency of hits using keywords
        </CardSubtitle>
        {/* <Chart
          type="area"
          width="100%"
          height="390"
          options={chartoptions.options}
          series={chartoptions.series}
        ></Chart> */}
        {chartoptions ? (
          <Chart
            type="area"
            width="100%"
            height="390"
            options={chartoptions.options}
            series={chartoptions.series}
          />
        ) : (
          <p>Loading chart data...</p>
        )}
      </CardBody>
    </Card>
  );
};

export default SalesChart;
