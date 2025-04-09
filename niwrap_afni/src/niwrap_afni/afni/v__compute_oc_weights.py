# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__COMPUTE_OC_WEIGHTS_METADATA = Metadata(
    id="8cbef05597be3ac05a382bf27e8ef50be3a6cef0.boutiques",
    name="@compute_OC_weights",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VComputeOcWeightsParameters = typing.TypedDict('VComputeOcWeightsParameters', {
    "__STYX_TYPE__": typing.Literal["@compute_OC_weights"],
    "echo_times": typing.NotRequired[str | None],
    "echo_times_file": typing.NotRequired[InputPathType | None],
    "echo_dsets": list[str],
    "prefix": typing.NotRequired[str | None],
    "def_to_equal": typing.NotRequired[str | None],
    "oc_method": typing.NotRequired[str | None],
    "sum_weight_tolerance": typing.NotRequired[float | None],
    "t2_star_limit": typing.NotRequired[float | None],
    "work_dir": typing.NotRequired[str | None],
    "verbosity": bool,
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
        "@compute_OC_weights": v__compute_oc_weights_cargs,
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
        "@compute_OC_weights": v__compute_oc_weights_outputs,
    }.get(t)


class VComputeOcWeightsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__compute_oc_weights(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_oc_weights: OutputPathType | None
    """Resulting OC weights dataset"""


def v__compute_oc_weights_params(
    echo_dsets: list[str],
    echo_times: str | None = None,
    echo_times_file: InputPathType | None = None,
    prefix: str | None = None,
    def_to_equal: str | None = None,
    oc_method: str | None = None,
    sum_weight_tolerance: float | None = None,
    t2_star_limit: float | None = None,
    work_dir: str | None = None,
    verbosity: bool = False,
) -> VComputeOcWeightsParameters:
    """
    Build parameters.
    
    Args:
        echo_dsets: Specify one run of multi-echo EPI data.
        echo_times: Specify echo times as list (e.g., "15 30.5 41"). Use either\
            -echo_times or -echo_times_files.
        echo_times_file: Specify file with echo times. Use either -echo_times\
            or -echo_times_files.
        prefix: Specify prefix of resulting OC weights dataset (e.g.,\
            OC.weights.SUBJ).
        def_to_equal: Specify whether to default to equal weights (default =\
            no).
        oc_method: Specify which OC method to employ (default = OC_A).
        sum_weight_tolerance: Tolerance for summed weight difference from 1.0\
            (default = 0.001).
        t2_star_limit: Specify limit for T2* values (default = 300).
        work_dir: Specify directory to compute results in.
        verbosity: Increase verbosity of output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@compute_OC_weights",
        "echo_dsets": echo_dsets,
        "verbosity": verbosity,
    }
    if echo_times is not None:
        params["echo_times"] = echo_times
    if echo_times_file is not None:
        params["echo_times_file"] = echo_times_file
    if prefix is not None:
        params["prefix"] = prefix
    if def_to_equal is not None:
        params["def_to_equal"] = def_to_equal
    if oc_method is not None:
        params["oc_method"] = oc_method
    if sum_weight_tolerance is not None:
        params["sum_weight_tolerance"] = sum_weight_tolerance
    if t2_star_limit is not None:
        params["t2_star_limit"] = t2_star_limit
    if work_dir is not None:
        params["work_dir"] = work_dir
    return params


def v__compute_oc_weights_cargs(
    params: VComputeOcWeightsParameters,
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
    cargs.append("@compute_OC_weights")
    if params.get("echo_times") is not None:
        cargs.extend([
            "-echo_times",
            params.get("echo_times")
        ])
    if params.get("echo_times_file") is not None:
        cargs.extend([
            "-echo_times_file",
            execution.input_file(params.get("echo_times_file"))
        ])
    cargs.extend([
        "-echo_dsets",
        *params.get("echo_dsets")
    ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("def_to_equal") is not None:
        cargs.extend([
            "-def_to_equal",
            params.get("def_to_equal")
        ])
    if params.get("oc_method") is not None:
        cargs.extend([
            "-oc_method",
            params.get("oc_method")
        ])
    if params.get("sum_weight_tolerance") is not None:
        cargs.extend([
            "-sum_weight_tolerance",
            str(params.get("sum_weight_tolerance"))
        ])
    if params.get("t2_star_limit") is not None:
        cargs.extend([
            "-t2_star_limit",
            str(params.get("t2_star_limit"))
        ])
    if params.get("work_dir") is not None:
        cargs.extend([
            "-work_dir",
            params.get("work_dir")
        ])
    if params.get("verbosity"):
        cargs.append("-verb")
    return cargs


def v__compute_oc_weights_outputs(
    params: VComputeOcWeightsParameters,
    execution: Execution,
) -> VComputeOcWeightsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VComputeOcWeightsOutputs(
        root=execution.output_file("."),
        output_oc_weights=execution.output_file(params.get("prefix") + "+tlrc.HEAD") if (params.get("prefix") is not None) else None,
    )
    return ret


def v__compute_oc_weights_execute(
    params: VComputeOcWeightsParameters,
    execution: Execution,
) -> VComputeOcWeightsOutputs:
    """
    Compute optimal combined weights dataset for multi-echo EPI data.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VComputeOcWeightsOutputs`).
    """
    params = execution.params(params)
    cargs = v__compute_oc_weights_cargs(params, execution)
    ret = v__compute_oc_weights_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__compute_oc_weights(
    echo_dsets: list[str],
    echo_times: str | None = None,
    echo_times_file: InputPathType | None = None,
    prefix: str | None = None,
    def_to_equal: str | None = None,
    oc_method: str | None = None,
    sum_weight_tolerance: float | None = None,
    t2_star_limit: float | None = None,
    work_dir: str | None = None,
    verbosity: bool = False,
    runner: Runner | None = None,
) -> VComputeOcWeightsOutputs:
    """
    Compute optimal combined weights dataset for multi-echo EPI data.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        echo_dsets: Specify one run of multi-echo EPI data.
        echo_times: Specify echo times as list (e.g., "15 30.5 41"). Use either\
            -echo_times or -echo_times_files.
        echo_times_file: Specify file with echo times. Use either -echo_times\
            or -echo_times_files.
        prefix: Specify prefix of resulting OC weights dataset (e.g.,\
            OC.weights.SUBJ).
        def_to_equal: Specify whether to default to equal weights (default =\
            no).
        oc_method: Specify which OC method to employ (default = OC_A).
        sum_weight_tolerance: Tolerance for summed weight difference from 1.0\
            (default = 0.001).
        t2_star_limit: Specify limit for T2* values (default = 300).
        work_dir: Specify directory to compute results in.
        verbosity: Increase verbosity of output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VComputeOcWeightsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__COMPUTE_OC_WEIGHTS_METADATA)
    params = v__compute_oc_weights_params(
        echo_times=echo_times,
        echo_times_file=echo_times_file,
        echo_dsets=echo_dsets,
        prefix=prefix,
        def_to_equal=def_to_equal,
        oc_method=oc_method,
        sum_weight_tolerance=sum_weight_tolerance,
        t2_star_limit=t2_star_limit,
        work_dir=work_dir,
        verbosity=verbosity,
    )
    return v__compute_oc_weights_execute(params, execution)


__all__ = [
    "VComputeOcWeightsOutputs",
    "VComputeOcWeightsParameters",
    "V__COMPUTE_OC_WEIGHTS_METADATA",
    "v__compute_oc_weights",
    "v__compute_oc_weights_params",
]
