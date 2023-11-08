import React, { useState } from "react";
import {
  Alert,
  UncontrolledAlert,
  Card,
  CardBody,
  CardTitle,
} from "reactstrap";

const Companythree = () => {
  // For Dismiss Button with Alert
  const [visible, setVisible] = useState(true);

  const onDismiss = () => {
    setVisible(false);
  };

  return (
    <div>
      {/* --------------------------------------------------------------------------------*/}
      {/* Card-1*/}
      {/* --------------------------------------------------------------------------------*/}
      <Card>
        <CardTitle tag="h6" className="border-bottom p-3 mb-0">
          <i className="bi bi-bell me-2"> </i>
          Company #1 info
        </CardTitle>
        <CardBody className="">
          <div className="mt-3">
            <h3>Replace this with company summary from backend</h3>
          </div>
        </CardBody>
      </Card>
      {/* --------------------------------------------------------------------------------*/}
      {/* Card-2*/}
      {/* --------------------------------------------------------------------------------*/}
      <Card>
        <CardTitle tag="h6" className="border-bottom p-3 mb-0">
          <i className="bi bi-bell me-2" />
          company summary #2
        </CardTitle>
        <CardBody className="">
          <div>
            <h3></h3>
          </div>
        </CardBody>
      </Card>
      {/* --------------------------------------------------------------------------------*/}
      {/* Card-3*/}
      {/* --------------------------------------------------------------------------------*/}
      <Card>
        <CardTitle tag="h6" className="border-bottom p-3 mb-0">
          <i className="bi bi-bell me-2" />
          summary #3
        </CardTitle>
        <CardBody className="">
          <div>
            {/* <Alert color="success">
              <h4 className="alert-heading">Well done!</h4>
              <p>
                Aww yeah, you successfully read this important alert message.
                This example text is going to run a bit longer so that you can
                see how spacing within an alert works with this kind of content.
              </p>
              <hr />
              <p className="mb-0">
                Whenever you need to, be sure to use margin utilities to keep
                things nice and tidy.
              </p>
            </Alert> */}
            <h3>add</h3>
          </div>
        </CardBody>
      </Card>
      {/* --------------------------------------------------------------------------------
      {/* Card-4*/}
      {/* --------------------------------------------------------------------------------*/}
      {/* <Card>
        <CardTitle tag="h6" className="border-bottom p-3 mb-0">
          <i className="bi bi-bell me-2" />
          Alert with Dissmissing
        </CardTitle>
        <CardBody className="">
          <div>
            <Alert color="info" isOpen={visible} toggle={onDismiss.bind(null)}>
              I am an alert and I can be dismissed!
            </Alert>
          </div>
        </CardBody>
      </Card> */}
      {/* --------------------------------------------------------------------------------*/}
      {/* Card-5*/}
      {/* --------------------------------------------------------------------------------*/}
      {/* <Card>
        <CardTitle tag="h6" className="border-bottom p-3 mb-0">
          <i className="bi bi-bell me-2" />
          Alert with Uncontrolled [disable] Alerts
        </CardTitle>
        <CardBody className="">
          <div>
            <UncontrolledAlert color="info">
              I am an alert and I can be dismissed!
            </UncontrolledAlert>
          </div>
        </CardBody>
      </Card> */}
      {/* --------------------------------------------------------------------------------*/}
      {/* Card-6*/}
      {/* --------------------------------------------------------------------------------*/}
      {/* <Card>
        <CardTitle tag="h6" className="border-bottom p-3 mb-0">
          <i className="bi bi-bell me-2" />
          Alerts without fade
        </CardTitle>
        <CardBody className="">
          <div>
            <Alert
              color="primary"
              isOpen={visible}
              toggle={onDismiss.bind(null)}
              fade={false}
            >
              I am a primary alert and I can be dismissed without animating!
            </Alert>
            <UncontrolledAlert color="warning" fade={false}>
              I am an alert and I can be dismissed without animating!
            </UncontrolledAlert>
          </div>
        </CardBody>
      </Card>  */}

      {/* --------------------------------------------------------------------------------*/}
      {/* End Inner Div*/}
      {/* --------------------------------------------------------------------------------*/}
    </div>
  );
};

export default Companythree;
