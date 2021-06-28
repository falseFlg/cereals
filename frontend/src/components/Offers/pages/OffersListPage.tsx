import React from "react";
import { useCallback } from "react";
import { generatePath, useHistory } from "react-router-dom";
import { useOffers } from "../../../hooks/useOffers";
import { useWarehouses } from "../../../hooks/useWarehouses";
import { routes } from "../../../routes/consts";
import { IOffer } from "../../../services/models";
import { Button, Flex, Spacer, Tabs, Typography } from "../../../uikit";
import { Card } from "../../../uikit/Card/Card";
import { Table } from "../../../uikit/Table/Table";
import { ITab } from "../../../uikit/Tabs/Tabs";
import { formatDate, formatMoney } from "../../../utils/utils";

export const OffersListPage: React.FC = () => {
  const { data } = useOffers();
  const history = useHistory();
  const { data: warehouseData } = useWarehouses();
  const offerData = data || [];

  const handleOfferClick = (id: string | number) => {
    history.push(generatePath(routes.offers.edit.path, { id }));
  };

  const handleCreateOffer = () => {
    history.push(generatePath(routes.offers.create.path));
  };

  const getWareHouseName = (warehouseId: number) =>
    warehouseData?.find((warehouse) => warehouse?.id === warehouseId)?.title;

  const renderOfferTab = useCallback(
    (data: IOffer[]): ITab => {
      const tab = {
        label: `${data?.[0]?.status} - ${data?.length}`,
        items: data?.map((item) => {
          const {
            title,
            volume,
            cost_with_NDS,
            cost,
            period_of_export,
            date_finish_shipment,
            date_start_shipment,
            warehouse,
            id,
          } = item || {};

          const periodOfShippment = `${formatDate(
            date_start_shipment
          )} — ${formatDate(date_finish_shipment)} (${period_of_export} дней)`;

          const dataList = [
            {
              title: "Объем, т",
              content: [volume],
            },
            {
              title: "Цена покупателя, руб",
              content: [
                `${formatMoney(cost)} без НДС / CNCPT`,
                `${formatMoney(cost_with_NDS)} с НДС / CVCPT`,
              ],
            },
            {
              title: "Период поставки",
              content: [periodOfShippment],
            },
            {
              title: "Порт",
              content: [getWareHouseName(warehouse)],
            },
          ];
          return (
            <Card title={title} onClick={() => handleOfferClick(id)}>
              <Spacer space={30} />
              <Table data={dataList} />
            </Card>
          );
        }),
      };
      return tab;
    },
    [warehouseData]
  );

  const activeData = renderOfferTab(
    offerData?.filter((el) => el.status === "active")
  );
  const archiveData = renderOfferTab(
    offerData?.filter((el) => el.status === "archive")
  );

  return (
    <Flex column>
      <Typography size="lg2" bold>
        Мои предложения
      </Typography>
      <Spacer space={28} />
      <Button variant="base" onClick={handleCreateOffer}>
        Создать предложение
      </Button>
      <Spacer space={28} />
      <Tabs tabs={[activeData, archiveData]} />
    </Flex>
  );
};