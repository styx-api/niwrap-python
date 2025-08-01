# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3DMASK_SVD_METADATA = Metadata(
    id="d590df9b7bd7af7769a60fa5f7ef2b1ffe4dc148.boutiques",
    name="3dmaskSVD",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dmaskSvdParameters = typing.TypedDict('V3dmaskSvdParameters', {
    "__STYXTYPE__": typing.Literal["3dmaskSVD"],
    "input_dataset": InputPathType,
    "vnorm": bool,
    "sval": typing.NotRequired[float | None],
    "mask_file": typing.NotRequired[InputPathType | None],
    "automask": bool,
    "polort": typing.NotRequired[float | None],
    "bandpass": typing.NotRequired[list[str] | None],
    "ort": typing.NotRequired[list[InputPathType] | None],
    "alt_input": typing.NotRequired[InputPathType | None],
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
        "3dmaskSVD": v_3dmask_svd_cargs,
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
        "3dmaskSVD": v_3dmask_svd_outputs,
    }.get(t)


class V3dmaskSvdOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dmask_svd(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    svd_output: OutputPathType
    """Singular vector output redirected to this file"""


def v_3dmask_svd_params(
    input_dataset: InputPathType,
    vnorm: bool = False,
    sval: float | None = None,
    mask_file: InputPathType | None = None,
    automask: bool = False,
    polort: float | None = None,
    bandpass: list[str] | None = None,
    ort: list[InputPathType] | None = None,
    alt_input: InputPathType | None = None,
) -> V3dmaskSvdParameters:
    """
    Build parameters.
    
    Args:
        input_dataset: Input dataset.
        vnorm: L2 normalize all time series before SVD.
        sval: Output singular vectors 0 .. a (default a=0 = first one only).
        mask_file: Define the mask (default is entire dataset).
        automask: Automatic mask definition.
        polort: Remove polynomial trend (default 0 if not specified).
        bandpass: Bandpass filter (mutually exclusive with -polort).
        ort: Time series to remove from the data before SVD-ization. You can\
            give more than 1 '-ort' option. 'xx.1D' can contain more than 1 column.
        alt_input: Alternative way to give the input dataset name.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dmaskSVD",
        "input_dataset": input_dataset,
        "vnorm": vnorm,
        "automask": automask,
    }
    if sval is not None:
        params["sval"] = sval
    if mask_file is not None:
        params["mask_file"] = mask_file
    if polort is not None:
        params["polort"] = polort
    if bandpass is not None:
        params["bandpass"] = bandpass
    if ort is not None:
        params["ort"] = ort
    if alt_input is not None:
        params["alt_input"] = alt_input
    return params


def v_3dmask_svd_cargs(
    params: V3dmaskSvdParameters,
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
    cargs.append("3dmaskSVD")
    cargs.append(execution.input_file(params.get("input_dataset")))
    if params.get("vnorm"):
        cargs.append("-vnorm")
    if params.get("sval") is not None:
        cargs.extend([
            "-sval",
            str(params.get("sval"))
        ])
    if params.get("mask_file") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask_file"))
        ])
    if params.get("automask"):
        cargs.append("-automask")
    if params.get("polort") is not None:
        cargs.extend([
            "-polort",
            str(params.get("polort"))
        ])
    if params.get("bandpass") is not None:
        cargs.extend([
            "-bpass",
            *params.get("bandpass")
        ])
    if params.get("ort") is not None:
        cargs.extend([
            "-ort",
            *[execution.input_file(f) for f in params.get("ort")]
        ])
    if params.get("alt_input") is not None:
        cargs.extend([
            "-input",
            execution.input_file(params.get("alt_input"))
        ])
    return cargs


def v_3dmask_svd_outputs(
    params: V3dmaskSvdParameters,
    execution: Execution,
) -> V3dmaskSvdOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dmaskSvdOutputs(
        root=execution.output_file("."),
        svd_output=execution.output_file("../stdout"),
    )
    return ret


def v_3dmask_svd_execute(
    params: V3dmaskSvdParameters,
    execution: Execution,
) -> V3dmaskSvdOutputs:
    """
    Computes the principal singular vector of the time series vectors extracted from
    the input dataset over the input mask.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dmaskSvdOutputs`).
    """
    params = execution.params(params)
    cargs = v_3dmask_svd_cargs(params, execution)
    ret = v_3dmask_svd_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3dmask_svd(
    input_dataset: InputPathType,
    vnorm: bool = False,
    sval: float | None = None,
    mask_file: InputPathType | None = None,
    automask: bool = False,
    polort: float | None = None,
    bandpass: list[str] | None = None,
    ort: list[InputPathType] | None = None,
    alt_input: InputPathType | None = None,
    runner: Runner | None = None,
) -> V3dmaskSvdOutputs:
    """
    Computes the principal singular vector of the time series vectors extracted from
    the input dataset over the input mask.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Input dataset.
        vnorm: L2 normalize all time series before SVD.
        sval: Output singular vectors 0 .. a (default a=0 = first one only).
        mask_file: Define the mask (default is entire dataset).
        automask: Automatic mask definition.
        polort: Remove polynomial trend (default 0 if not specified).
        bandpass: Bandpass filter (mutually exclusive with -polort).
        ort: Time series to remove from the data before SVD-ization. You can\
            give more than 1 '-ort' option. 'xx.1D' can contain more than 1 column.
        alt_input: Alternative way to give the input dataset name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dmaskSvdOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DMASK_SVD_METADATA)
    params = v_3dmask_svd_params(
        input_dataset=input_dataset,
        vnorm=vnorm,
        sval=sval,
        mask_file=mask_file,
        automask=automask,
        polort=polort,
        bandpass=bandpass,
        ort=ort,
        alt_input=alt_input,
    )
    return v_3dmask_svd_execute(params, execution)


__all__ = [
    "V3dmaskSvdOutputs",
    "V3dmaskSvdParameters",
    "V_3DMASK_SVD_METADATA",
    "v_3dmask_svd",
    "v_3dmask_svd_params",
]
