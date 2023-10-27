import { Row, Col, Card, CardBody, CardTitle } from "reactstrap";

const About = () => {
  return (
    <Row>
      <Col>
        {/* --------------------------------------------------------------------------------*/}
        {/* Card-1*/}
        {/* --------------------------------------------------------------------------------*/}
        <Card>
          <CardTitle tag="h6" className="border-bottom p-3 mb-0">
            <i className="bi bi-bell me-2"> </i>
            About this project
          </CardTitle>
          <CardBody className="p-4">
            <Row>
              <Col lg="8">
                <h2 className="mt-4">Fusion Fund</h2>
                <h5 className=" mb-4">
                This website provides insight for AI companies
                </h5>
                <img
                  src="https://www.wrappixel.com/wp-content/uploads/edd/2020/09/ample-react-admin-template-y.png"
                  alt="my" className="w-100"
                />

              </Col>
            </Row>
          </CardBody>
        </Card>
      </Col>
    </Row>
  );
};

export default About;
