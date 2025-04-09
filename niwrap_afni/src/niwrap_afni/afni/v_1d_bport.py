# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_1D_BPORT_METADATA = Metadata(
    id="43a3106d2b925d564ce642121a3f6c7f7d191ebb.boutiques",
    name="1dBport",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V1dBportParameters = typing.TypedDict('V1dBportParameters', {
    "__STYX_TYPE__": typing.Literal["1dBport"],
    "band": list[float],
    "invert": bool,
    "nozero": bool,
    "noconst": bool,
    "quad": bool,
    "input_dataset": typing.NotRequired[InputPathType | None],
    "input_1d_file": typing.NotRequired[InputPathType | None],
    "nodata": typing.NotRequired[list[float] | None],
    "tr": typing.NotRequired[float | None],
    "concat": typing.NotRequired[InputPathType | None],
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
        "1dBport": v_1d_bport_cargs,
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
        "1dBport": v_1d_bport_outputs,
    }.get(t)


class V1dBportOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1d_bport(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    stdout: OutputPathType
    """Standard output file written by the tool"""


def v_1d_bport_params(
    band: list[float],
    invert: bool = False,
    nozero: bool = False,
    noconst: bool = False,
    quad: bool = False,
    input_dataset: InputPathType | None = None,
    input_1d_file: InputPathType | None = None,
    nodata: list[float] | None = None,
    tr: float | None = None,
    concat: InputPathType | None = None,
) -> V1dBportParameters:
    """
    Build parameters.
    
    Args:
        band: Specify lowest and highest frequencies in the passband.
        invert: Invert the selection after computing which frequency indexes\
            correspond to the input band(s).
        nozero: Do NOT generate the 0 frequency (constant) component when fbot\
            = 0.
        noconst: Same as -nozero. Do NOT generate the 0 frequency (constant)\
            component when fbot = 0.
        quad: Add regressors for linear and quadratic trends.
        input_dataset: Specify the dataset input.
        input_1d_file: Specify the 1D input file.
        nodata: Specify the number of time points and optionally TR value for\
            the simulation.
        tr: Set the time step duration.
        concat: Specify the list of start indexes for concatenated runs.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "1dBport",
        "band": band,
        "invert": invert,
        "nozero": nozero,
        "noconst": noconst,
        "quad": quad,
    }
    if input_dataset is not None:
        params["input_dataset"] = input_dataset
    if input_1d_file is not None:
        params["input_1d_file"] = input_1d_file
    if nodata is not None:
        params["nodata"] = nodata
    if tr is not None:
        params["tr"] = tr
    if concat is not None:
        params["concat"] = concat
    return params


def v_1d_bport_cargs(
    params: V1dBportParameters,
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
    cargs.append("1dBport")
    cargs.extend([
        "-band",
        *map(str, params.get("band"))
    ])
    if params.get("invert"):
        cargs.append("-invert")
    if params.get("nozero"):
        cargs.append("-nozero")
    if params.get("noconst"):
        cargs.append("-noconst")
    if params.get("quad"):
        cargs.append("-quad")
    if params.get("input_dataset") is not None:
        cargs.extend([
            "-input",
            execution.input_file(params.get("input_dataset"))
        ])
    if params.get("input_1d_file") is not None:
        cargs.extend([
            "-input1D",
            execution.input_file(params.get("input_1d_file"))
        ])
    if params.get("nodata") is not None:
        cargs.extend([
            "-nodata",
            *map(str, params.get("nodata"))
        ])
    if params.get("tr") is not None:
        cargs.extend([
            "-TR",
            str(params.get("tr"))
        ])
    if params.get("concat") is not None:
        cargs.extend([
            "-concat",
            execution.input_file(params.get("concat"))
        ])
    return cargs


def v_1d_bport_outputs(
    params: V1dBportParameters,
    execution: Execution,
) -> V1dBportOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V1dBportOutputs(
        root=execution.output_file("."),
        stdout=execution.output_file("stdout"),
    )
    return ret


def v_1d_bport_execute(
    params: V1dBportParameters,
    execution: Execution,
) -> V1dBportOutputs:
    """
    Creates a set of columns of sines and cosines for bandpassing via regression.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V1dBportOutputs`).
    """
    params = execution.params(params)
    cargs = v_1d_bport_cargs(params, execution)
    ret = v_1d_bport_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_1d_bport(
    band: list[float],
    invert: bool = False,
    nozero: bool = False,
    noconst: bool = False,
    quad: bool = False,
    input_dataset: InputPathType | None = None,
    input_1d_file: InputPathType | None = None,
    nodata: list[float] | None = None,
    tr: float | None = None,
    concat: InputPathType | None = None,
    runner: Runner | None = None,
) -> V1dBportOutputs:
    """
    Creates a set of columns of sines and cosines for bandpassing via regression.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        band: Specify lowest and highest frequencies in the passband.
        invert: Invert the selection after computing which frequency indexes\
            correspond to the input band(s).
        nozero: Do NOT generate the 0 frequency (constant) component when fbot\
            = 0.
        noconst: Same as -nozero. Do NOT generate the 0 frequency (constant)\
            component when fbot = 0.
        quad: Add regressors for linear and quadratic trends.
        input_dataset: Specify the dataset input.
        input_1d_file: Specify the 1D input file.
        nodata: Specify the number of time points and optionally TR value for\
            the simulation.
        tr: Set the time step duration.
        concat: Specify the list of start indexes for concatenated runs.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dBportOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1D_BPORT_METADATA)
    params = v_1d_bport_params(
        band=band,
        invert=invert,
        nozero=nozero,
        noconst=noconst,
        quad=quad,
        input_dataset=input_dataset,
        input_1d_file=input_1d_file,
        nodata=nodata,
        tr=tr,
        concat=concat,
    )
    return v_1d_bport_execute(params, execution)


__all__ = [
    "V1dBportOutputs",
    "V1dBportParameters",
    "V_1D_BPORT_METADATA",
    "v_1d_bport",
    "v_1d_bport_params",
]
