from opentrons import protocol_api

metadata = {'apiLevel': '2.2',
            'protocolName': 'Purification Template v2',
            'author': 'Gabrielle Johnston',
            'description': 'DNABot updated purification template'}

sample_number = 0
ethanol_well = 1
elution_buffer_well = 1
p300_mount = 'left'
p300_type = 'p300_single'
p10_type = 'p10_single'
well_plate_type = '4ti_0960_framestar'
reagent_plate_type = 'usascientific_12_reservoir_22ml',
bead_container_type = 'usascientific_96_wellplate_2.4ml_deep'
multi = False

def run(protocol: protocol_api.ProtocolContext):
    def magbead(
        sample_number,
        ethanol_well,
        elution_buffer_well,
        sample_volume=30,
        bead_ratio=1.8,
        elution_buffer_volume=40,
        incubation_time=5,
        settling_time=120,
        drying_time=5,
        elution_time=2,
        sample_offset=0,
        tiprack_type='opentrons_96_tiprack_300ul',
        p300_mount='left',
        p300_type='p300_multi',
        well_plate_type='biorad_96_wellplate_200ul_pcr',
        reagent_plate_type='usascientific_12_reservoir_22ml',
        bead_container_type='usascientific_96_wellplate_2.4ml_deep',
        multi=True):
        """Implements magbead purification reactions for BASIC assembly using an opentrons OT-2.

        Selected args:
            ethanol_well (str): well in reagent container containing ethanol.
            elution_buffer_well (str): well in reagent container containing elution buffer.
            sample_offset (int): offset the intial sample column by the specified value.

        """

        # Constants
        # PIPETTE_MOUNT = 'left'
        PIPETTE_MOUNT = p300_mount
        PIPETTE_ASPIRATE_RATE = 25
        PIPETTE_DISPENSE_RATE = 150
        TIPS_PER_SAMPLE = 9
        CANDIDATE_TIPRACK_SLOTS = ['3', '6', '9', '2', '5']
        MAGDECK_POSITION = '1'
        # MIX_PLATE_TYPE = 'biorad_96_wellplate_200ul_pcr'
        MIX_PLATE_TYPE = well_plate_type
        MIX_PLATE_POSITION = '4'
        # REAGENT_CONTAINER_TYPE = 'usascientific_12_reservoir_22ml'
        REAGENT_CONTAINER_TYPE = reagent_plate_type
        REAGENT_CONTAINER_POSITION = '7'
        # BEAD_CONTAINER_TYPE = 'usascientific_96_wellplate_2.4ml_deep'
        BEAD_CONTAINER_TYPE = bead_container_type
        BEAD_CONTAINER_POSITION = '8'
        LIQUID_WASTE_WELL = 'A12'
        BEADS_WELL = 'A1'
        DEAD_TOTAL_VOL = 5
        SLOW_HEAD_SPEEDS = {'x': 600 // 4, 'y': 400 // 4,
                            'z': 125 // 10, 'a': 125 // 10}
        DEFAULT_HEAD_SPEEDS = {'x': 400, 'y': 400, 'z': 125, 'a': 100}
        IMMOBILISE_MIX_REPS = 10
        MAGDECK_HEIGHT = 20
        AIR_VOL_COEFF = 0.1
        ETHANOL_VOL = 150
        WASH_TIME = 0.5
        ETHANOL_DEAD_VOL = 50
        ELUTION_MIX_REPS = 20
        ELUTANT_SEP_TIME = 1
        ELUTION_DEAD_VOL = 2

        # Define labware
        total_tips = 96
        tiprack_num = total_tips // 96 + (1 if total_tips % 96 > 0 else 0)
        slots = CANDIDATE_TIPRACK_SLOTS[:tiprack_num]
        tipracks = [protocol.load_labware(tiprack_type, slot)
                    for slot in slots]
        pipette = protocol.load_instrument(p10_type, PIPETTE_MOUNT,
                                           tip_racks=tipracks)
        mag_mod = protocol.load_module('magnetic module', MAGDECK_POSITION)

        # Engagae MagDeck and incubate
        mag_mod.engage(height=MAGDECK_HEIGHT)
        protocol.delay(minutes=settling_time)

        # Disengage MagDeck
        mag_mod.disengage()

    magbead(sample_number=sample_number,
            ethanol_well=ethanol_well, elution_buffer_well='A1',
            p300_mount=p300_mount, p300_type=p300_type,
            well_plate_type=well_plate_type, reagent_plate_type=reagent_plate_type,
            bead_container_type=bead_container_type, multi=multi)
