# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

POSSUM_METADATA = Metadata(
    id="24b08ea6c03b4298ab43a4f36dc382ae9b1cf2dc.boutiques",
    name="possum",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


PossumParameters = typing.TypedDict('PossumParameters', {
    "__STYX_TYPE__": typing.Literal["possum"],
    "input_volume": InputPathType,
    "mr_parameters": InputPathType,
    "motion_matrix": InputPathType,
    "pulse_sequence": str,
    "rf_slice_profile": InputPathType,
    "output_signal": str,
    "event_matrix": InputPathType,
    "verbose": bool,
    "help": bool,
    "kcoord": bool,
    "b0_inhomogeneities": typing.NotRequired[str | None],
    "extra_b0_inhomogeneities": typing.NotRequired[InputPathType | None],
    "b0_inhomogeneities_timecourse": typing.NotRequired[InputPathType | None],
    "rf_inhomogeneity_receive": typing.NotRequired[InputPathType | None],
    "rf_inhomogeneity_transmit": typing.NotRequired[InputPathType | None],
    "activation_volume": typing.NotRequired[InputPathType | None],
    "activation_timecourse": typing.NotRequired[InputPathType | None],
    "activation_4d_volume": typing.NotRequired[InputPathType | None],
    "activation_4d_timecourse": typing.NotRequired[InputPathType | None],
    "level": typing.NotRequired[str | None],
    "num_procs": typing.NotRequired[float | None],
    "proc_id": typing.NotRequired[float | None],
    "no_speedup": bool,
    "rf_average": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "possum": possum_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "possum": possum_outputs,
    }.get(t)


class PossumOutputs(typing.NamedTuple):
    """
    Output object returned when calling `possum(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_matrix: OutputPathType
    """Output matrix file generated by possum"""


def possum_params(
    input_volume: InputPathType,
    mr_parameters: InputPathType,
    motion_matrix: InputPathType,
    pulse_sequence: str,
    rf_slice_profile: InputPathType,
    output_signal: str,
    event_matrix: InputPathType,
    verbose: bool = False,
    help_: bool = False,
    kcoord: bool = False,
    b0_inhomogeneities: str | None = None,
    extra_b0_inhomogeneities: InputPathType | None = None,
    b0_inhomogeneities_timecourse: InputPathType | None = None,
    rf_inhomogeneity_receive: InputPathType | None = None,
    rf_inhomogeneity_transmit: InputPathType | None = None,
    activation_volume: InputPathType | None = None,
    activation_timecourse: InputPathType | None = None,
    activation_4d_volume: InputPathType | None = None,
    activation_4d_timecourse: InputPathType | None = None,
    level: str | None = None,
    num_procs: float | None = None,
    proc_id: float | None = None,
    no_speedup: bool = False,
    rf_average: bool = False,
) -> PossumParameters:
    """
    Build parameters.
    
    Args:
        input_volume: Input 4D volume filename.
        mr_parameters: Input matrix filename containing MR parameters.
        motion_matrix: Input motion matrix filename (time(s) Tx(m) Ty(m) Tz(m)\
            Rx(rad) Ry(rad) Rz(rad)).
        pulse_sequence: Input matrix basename for pulse sequence files (.posx,\
            .posy, etc.).
        rf_slice_profile: Input matrix filename containing RF slice profile.
        output_signal: Output matrix filename for the signal.
        event_matrix: Main event matrix file [(t(s), rf_ang(rad),\
            rf_freq_band(Hz), rf_cent_freq(Hz), ...)].
        verbose: Switch on diagnostic messages.
        help_: Display help message.
        kcoord: Save the k-space coordinates.
        b0_inhomogeneities: B0 inhomogeneities due to susceptibility\
            differences (basename).
        extra_b0_inhomogeneities: B0 inhomogeneities due to an extra field.
        b0_inhomogeneities_timecourse: B0 inhomogeneities timecourse file.
        rf_inhomogeneity_receive: RF inhomogeneity - receive.
        rf_inhomogeneity_transmit: RF inhomogeneity - transmit.
        activation_volume: Activation volume file.
        activation_timecourse: Activation time course file.
        activation_4d_volume: Activation 4D volume file.
        activation_4d_timecourse: Activation 4D time course file.
        level: Level of processing: 1.no motion//basic B0, 2.motion//basic B0,\
            3.motion//full B0, 4.no motion//time changing B0.
        num_procs: Number of processors available for parallelisation.
        proc_id: ID of the processor.
        no_speedup: If ON, will not do the speedup but perform signal\
            calculation for all slices for each voxel.
        rf_average: If ON, it will use RF angle averaging.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "possum",
        "input_volume": input_volume,
        "mr_parameters": mr_parameters,
        "motion_matrix": motion_matrix,
        "pulse_sequence": pulse_sequence,
        "rf_slice_profile": rf_slice_profile,
        "output_signal": output_signal,
        "event_matrix": event_matrix,
        "verbose": verbose,
        "help": help_,
        "kcoord": kcoord,
        "no_speedup": no_speedup,
        "rf_average": rf_average,
    }
    if b0_inhomogeneities is not None:
        params["b0_inhomogeneities"] = b0_inhomogeneities
    if extra_b0_inhomogeneities is not None:
        params["extra_b0_inhomogeneities"] = extra_b0_inhomogeneities
    if b0_inhomogeneities_timecourse is not None:
        params["b0_inhomogeneities_timecourse"] = b0_inhomogeneities_timecourse
    if rf_inhomogeneity_receive is not None:
        params["rf_inhomogeneity_receive"] = rf_inhomogeneity_receive
    if rf_inhomogeneity_transmit is not None:
        params["rf_inhomogeneity_transmit"] = rf_inhomogeneity_transmit
    if activation_volume is not None:
        params["activation_volume"] = activation_volume
    if activation_timecourse is not None:
        params["activation_timecourse"] = activation_timecourse
    if activation_4d_volume is not None:
        params["activation_4d_volume"] = activation_4d_volume
    if activation_4d_timecourse is not None:
        params["activation_4d_timecourse"] = activation_4d_timecourse
    if level is not None:
        params["level"] = level
    if num_procs is not None:
        params["num_procs"] = num_procs
    if proc_id is not None:
        params["proc_id"] = proc_id
    return params


def possum_cargs(
    params: PossumParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("possum")
    cargs.extend([
        "--inp",
        execution.input_file(params.get("input_volume"))
    ])
    cargs.extend([
        "--mrpar",
        execution.input_file(params.get("mr_parameters"))
    ])
    cargs.extend([
        "--motion",
        execution.input_file(params.get("motion_matrix"))
    ])
    cargs.extend([
        "--pulse",
        params.get("pulse_sequence")
    ])
    cargs.extend([
        "--slcprof",
        execution.input_file(params.get("rf_slice_profile"))
    ])
    cargs.extend([
        "--out",
        params.get("output_signal")
    ])
    cargs.extend([
        "--mainmatx",
        execution.input_file(params.get("event_matrix"))
    ])
    if params.get("verbose"):
        cargs.append("--verbose")
    if params.get("help"):
        cargs.append("--help")
    if params.get("kcoord"):
        cargs.append("--kcoord")
    if params.get("b0_inhomogeneities") is not None:
        cargs.extend([
            "--b0p",
            params.get("b0_inhomogeneities")
        ])
    if params.get("extra_b0_inhomogeneities") is not None:
        cargs.extend([
            "--b0extra",
            execution.input_file(params.get("extra_b0_inhomogeneities"))
        ])
    if params.get("b0_inhomogeneities_timecourse") is not None:
        cargs.extend([
            "--b0time",
            execution.input_file(params.get("b0_inhomogeneities_timecourse"))
        ])
    if params.get("rf_inhomogeneity_receive") is not None:
        cargs.extend([
            "--rfr",
            execution.input_file(params.get("rf_inhomogeneity_receive"))
        ])
    if params.get("rf_inhomogeneity_transmit") is not None:
        cargs.extend([
            "--rft",
            execution.input_file(params.get("rf_inhomogeneity_transmit"))
        ])
    if params.get("activation_volume") is not None:
        cargs.extend([
            "--activ",
            execution.input_file(params.get("activation_volume"))
        ])
    if params.get("activation_timecourse") is not None:
        cargs.extend([
            "--activt",
            execution.input_file(params.get("activation_timecourse"))
        ])
    if params.get("activation_4d_volume") is not None:
        cargs.extend([
            "--activ4D",
            execution.input_file(params.get("activation_4d_volume"))
        ])
    if params.get("activation_4d_timecourse") is not None:
        cargs.extend([
            "--activt4D",
            execution.input_file(params.get("activation_4d_timecourse"))
        ])
    if params.get("level") is not None:
        cargs.extend([
            "--lev",
            params.get("level")
        ])
    if params.get("num_procs") is not None:
        cargs.extend([
            "--nproc",
            str(params.get("num_procs"))
        ])
    if params.get("proc_id") is not None:
        cargs.extend([
            "--procid",
            str(params.get("proc_id"))
        ])
    if params.get("no_speedup"):
        cargs.append("--nospeedup")
    if params.get("rf_average"):
        cargs.append("--rfavg")
    return cargs


def possum_outputs(
    params: PossumParameters,
    execution: Execution,
) -> PossumOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = PossumOutputs(
        root=execution.output_file("."),
        output_matrix=execution.output_file("[OUTPUT_MATRIX].mat"),
    )
    return ret


def possum_execute(
    params: PossumParameters,
    execution: Execution,
) -> PossumOutputs:
    """
    Positron emission tomography (PET) simulation tool as part of FSL suite.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `PossumOutputs`).
    """
    params = execution.params(params)
    cargs = possum_cargs(params, execution)
    ret = possum_outputs(params, execution)
    execution.run(cargs)
    return ret


def possum(
    input_volume: InputPathType,
    mr_parameters: InputPathType,
    motion_matrix: InputPathType,
    pulse_sequence: str,
    rf_slice_profile: InputPathType,
    output_signal: str,
    event_matrix: InputPathType,
    verbose: bool = False,
    help_: bool = False,
    kcoord: bool = False,
    b0_inhomogeneities: str | None = None,
    extra_b0_inhomogeneities: InputPathType | None = None,
    b0_inhomogeneities_timecourse: InputPathType | None = None,
    rf_inhomogeneity_receive: InputPathType | None = None,
    rf_inhomogeneity_transmit: InputPathType | None = None,
    activation_volume: InputPathType | None = None,
    activation_timecourse: InputPathType | None = None,
    activation_4d_volume: InputPathType | None = None,
    activation_4d_timecourse: InputPathType | None = None,
    level: str | None = None,
    num_procs: float | None = None,
    proc_id: float | None = None,
    no_speedup: bool = False,
    rf_average: bool = False,
    runner: Runner | None = None,
) -> PossumOutputs:
    """
    Positron emission tomography (PET) simulation tool as part of FSL suite.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_volume: Input 4D volume filename.
        mr_parameters: Input matrix filename containing MR parameters.
        motion_matrix: Input motion matrix filename (time(s) Tx(m) Ty(m) Tz(m)\
            Rx(rad) Ry(rad) Rz(rad)).
        pulse_sequence: Input matrix basename for pulse sequence files (.posx,\
            .posy, etc.).
        rf_slice_profile: Input matrix filename containing RF slice profile.
        output_signal: Output matrix filename for the signal.
        event_matrix: Main event matrix file [(t(s), rf_ang(rad),\
            rf_freq_band(Hz), rf_cent_freq(Hz), ...)].
        verbose: Switch on diagnostic messages.
        help_: Display help message.
        kcoord: Save the k-space coordinates.
        b0_inhomogeneities: B0 inhomogeneities due to susceptibility\
            differences (basename).
        extra_b0_inhomogeneities: B0 inhomogeneities due to an extra field.
        b0_inhomogeneities_timecourse: B0 inhomogeneities timecourse file.
        rf_inhomogeneity_receive: RF inhomogeneity - receive.
        rf_inhomogeneity_transmit: RF inhomogeneity - transmit.
        activation_volume: Activation volume file.
        activation_timecourse: Activation time course file.
        activation_4d_volume: Activation 4D volume file.
        activation_4d_timecourse: Activation 4D time course file.
        level: Level of processing: 1.no motion//basic B0, 2.motion//basic B0,\
            3.motion//full B0, 4.no motion//time changing B0.
        num_procs: Number of processors available for parallelisation.
        proc_id: ID of the processor.
        no_speedup: If ON, will not do the speedup but perform signal\
            calculation for all slices for each voxel.
        rf_average: If ON, it will use RF angle averaging.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PossumOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(POSSUM_METADATA)
    params = possum_params(
        input_volume=input_volume,
        mr_parameters=mr_parameters,
        motion_matrix=motion_matrix,
        pulse_sequence=pulse_sequence,
        rf_slice_profile=rf_slice_profile,
        output_signal=output_signal,
        event_matrix=event_matrix,
        verbose=verbose,
        help_=help_,
        kcoord=kcoord,
        b0_inhomogeneities=b0_inhomogeneities,
        extra_b0_inhomogeneities=extra_b0_inhomogeneities,
        b0_inhomogeneities_timecourse=b0_inhomogeneities_timecourse,
        rf_inhomogeneity_receive=rf_inhomogeneity_receive,
        rf_inhomogeneity_transmit=rf_inhomogeneity_transmit,
        activation_volume=activation_volume,
        activation_timecourse=activation_timecourse,
        activation_4d_volume=activation_4d_volume,
        activation_4d_timecourse=activation_4d_timecourse,
        level=level,
        num_procs=num_procs,
        proc_id=proc_id,
        no_speedup=no_speedup,
        rf_average=rf_average,
    )
    return possum_execute(params, execution)


__all__ = [
    "POSSUM_METADATA",
    "PossumOutputs",
    "PossumParameters",
    "possum",
    "possum_params",
]
