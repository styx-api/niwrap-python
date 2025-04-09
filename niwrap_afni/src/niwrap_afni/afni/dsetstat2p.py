# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DSETSTAT2P_METADATA = Metadata(
    id="fb3a7f92243aa4cb63be144e3742b4a9615c1b61.boutiques",
    name="dsetstat2p",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


Dsetstat2pParameters = typing.TypedDict('Dsetstat2pParameters', {
    "__STYX_TYPE__": typing.Literal["dsetstat2p"],
    "dataset": str,
    "statval": float,
    "bisided": bool,
    "two_sided": bool,
    "one_sided": bool,
    "quiet": bool,
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
        "dsetstat2p": dsetstat2p_cargs,
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
        "dsetstat2p": dsetstat2p_outputs,
    }.get(t)


class Dsetstat2pOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dsetstat2p(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output p-value or stat value"""


def dsetstat2p_params(
    dataset: str,
    statval: float,
    bisided: bool = False,
    two_sided: bool = False,
    one_sided: bool = False,
    quiet: bool = False,
) -> Dsetstat2pParameters:
    """
    Build parameters.
    
    Args:
        dataset: Specify a dataset DDD and, if it has multiple sub-bricks, the\
            [i]th subbrick with the statistic of interest MUST be selected\
            explicitly; note the use of quotation marks around the brick selector\
            (because of the square-brackets). Note that 'i' can be either a number\
            of a string label selector.
        statval: Input stat-value S, which MUST be in the interval [0,\
            infinity).
        bisided: Choose one-sided or bi-sided/two-sided testing.
        two_sided: Choose one-sided or bi-sided/two-sided testing.
        one_sided: Choose one-sided or bi-sided/two-sided testing.
        quiet: An optional flag so that output ONLY the final statistic value\
            output to standard output; this can be then be viewed, redirected to a\
            text file or saved as a shell variable. (Default: display supplementary\
            text.).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dsetstat2p",
        "dataset": dataset,
        "statval": statval,
        "bisided": bisided,
        "two_sided": two_sided,
        "one_sided": one_sided,
        "quiet": quiet,
    }
    return params


def dsetstat2p_cargs(
    params: Dsetstat2pParameters,
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
    cargs.append("dsetstat2p")
    cargs.append(params.get("dataset"))
    cargs.append(str(params.get("statval")))
    if params.get("bisided"):
        cargs.append("-bisided")
    if params.get("two_sided"):
        cargs.append("-2sided")
    if params.get("one_sided"):
        cargs.append("-1sided")
    if params.get("quiet"):
        cargs.append("-quiet")
    return cargs


def dsetstat2p_outputs(
    params: Dsetstat2pParameters,
    execution: Execution,
) -> Dsetstat2pOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Dsetstat2pOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("output.txt"),
    )
    return ret


def dsetstat2p_execute(
    params: Dsetstat2pParameters,
    execution: Execution,
) -> Dsetstat2pOutputs:
    """
    Converts a statistic to a p-value with reference to a particular dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Dsetstat2pOutputs`).
    """
    params = execution.params(params)
    cargs = dsetstat2p_cargs(params, execution)
    ret = dsetstat2p_outputs(params, execution)
    execution.run(cargs)
    return ret


def dsetstat2p(
    dataset: str,
    statval: float,
    bisided: bool = False,
    two_sided: bool = False,
    one_sided: bool = False,
    quiet: bool = False,
    runner: Runner | None = None,
) -> Dsetstat2pOutputs:
    """
    Converts a statistic to a p-value with reference to a particular dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset: Specify a dataset DDD and, if it has multiple sub-bricks, the\
            [i]th subbrick with the statistic of interest MUST be selected\
            explicitly; note the use of quotation marks around the brick selector\
            (because of the square-brackets). Note that 'i' can be either a number\
            of a string label selector.
        statval: Input stat-value S, which MUST be in the interval [0,\
            infinity).
        bisided: Choose one-sided or bi-sided/two-sided testing.
        two_sided: Choose one-sided or bi-sided/two-sided testing.
        one_sided: Choose one-sided or bi-sided/two-sided testing.
        quiet: An optional flag so that output ONLY the final statistic value\
            output to standard output; this can be then be viewed, redirected to a\
            text file or saved as a shell variable. (Default: display supplementary\
            text.).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Dsetstat2pOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DSETSTAT2P_METADATA)
    params = dsetstat2p_params(
        dataset=dataset,
        statval=statval,
        bisided=bisided,
        two_sided=two_sided,
        one_sided=one_sided,
        quiet=quiet,
    )
    return dsetstat2p_execute(params, execution)


__all__ = [
    "DSETSTAT2P_METADATA",
    "Dsetstat2pOutputs",
    "Dsetstat2pParameters",
    "dsetstat2p",
    "dsetstat2p_params",
]
